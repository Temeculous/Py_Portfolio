from Linked_List import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
                current.next = Node(data)
    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

the_list = LinkedList()