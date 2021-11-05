# Create a New Node
class Node:
    def __init__(self, item):   # initialize the new node
        self.item = item
        self.next = None


# This Class implements the linked list.
class Linkedlist:
    def __init__(self):     # Initialize head to None
        self.head = None

    # Insert at the beginning
    def iab(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert after a Node
    def iafn(self, node, data):

        if node is None:
            print("the given node must be in linekedlist")
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    # Insert at the end
    def iatend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    # Deleting a Node
    def deleteNode(self, position):

        if self.head == None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

        # Find the key to be deleted
        for i in range(position-1):
            temp_node = temp_node.next
            if temp_node is None:
                break

        # if key is not present
        if temp_node is None:
            return

        if temp_node.next is None:
            return

        next = temp_node.next.next
        temp_node.next = None
        temp_node.next = next

    def printlist(self):
        temp_node = self.head
        while(temp_node):
            print(str(temp_node.item) + " ", end="")
            temp_node = temp_node.next


if __name__ == '__main__':
    llist = Linkedlist()
    llist.iatend(1)
    llist.iab(2)
    llist.iab(3)
    llist.iatend(4)
    llist.iafn(llist.head.next, 5)

    print('Linked list:')
    llist.printlist()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printlist()
