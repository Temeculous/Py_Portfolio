import random

# global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

game_on = True

# Classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'the deck has ' + deck_comp 

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        #if tally over 21 and there is an ace in hand, change ace value to 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chip:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        
        try:
            chips.bet = int(input('How many chips woould you like to bet?: '))
        except:
            print('Sorry please provide a number')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips for this bet!')
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_ace()

def hit_or_stand(deck, hand):
    global game_on

    while True:
        x = input('Hit or Stand? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn")
            game_on = False

        else:
            print("Sorry, I didn't understand, please enter an h or s")
            continue
        break

def show_some(player, dealer):
    
    # show 1  dealer card
    print('\n Dealer hand: ')
    print('First card hidden')
    print(dealer.cards[1])

    # show all player cards
    print('\n Player hand: ')
    for card in player.cards:
        print(card)

def show_all(player, dealer):

    # show all dealer cards
    print('\n Dealer hand: ', *dealer.cards, sep = '\n')

    print(f'Value of Dealer hand is: {dealer.value}')

    # show all player cards
    print('\n Player hand: ', *player.cards, sep = '\n')

    print(f'Value of Player hand is: {player.value}')

def player_bust(player, dealer, chips):
    print('Player BUST')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player WINS')
    chips.win_bet()

def dealer_bust(player, dealer, chips):
    print('Dealer BUST, Player WINS')
    chips.win_bet()

def dealer_wins(pleyer, dealer, chips):
    print('Dealer W?INS')
    chips.lose_bet()

def push(player, dealer, chips):
    print('Push, dealer and player tie')

while True:

    print('WELCOME TO BLACKJACK')

    deck = Deck()
    deck.shuffle_deck()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chip()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    hit_or_stand(deck, player_hand)

    show_some(player_hand, dealer_hand)

    if player_hand.value > 21:
        player_bust(player_hand, dealer_hand, player_chips)
        break

    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

        print('\n Player has {} total chips'.format(player_chips.total))

    new_game = input('Would you like to play another hand y/n?: ')
    if new_game[0].lower() == 'y':
        game_on = True
        continue
    else:
        print('Thank you for playing!')
        break