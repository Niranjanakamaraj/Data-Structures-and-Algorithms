class Node:
    def __init__(self, data):
        self.data = data                                    # Storing the data
        self.next = None                                    # Pointing to the next node

class CircularLinkedList:
    def __init__(self):
        self.head = None                                    # Initially the list is empty

    def insert(self, data):                                 # Inserting a new node at the end of the list
        new_node = Node(data)
        if self.head is None:                               # If the list is empty, make the new node the head
            self.head = new_node
            new_node.next = self.head                       # Pointing to head to make it circular
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node                            # Linking the last node to the new node
            new_node.next = self.head                       # Linking the new node back to the head

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:                      # Stop when we reach back to the head
                    break
            print("(back to head)")

def main():
    circular_linked_list = CircularLinkedList()            # Creating an empty circular linked list
    n = int(input("Enter the number of elements you want to insert: "))
    for i in range(n):
        data = int(input(f"Enter element {i+1}: "))
        circular_linked_list.insert(data)
    print("\nCircular Linked List:")
    circular_linked_list.display()
    
if __name__ == "__main__":
    main()
