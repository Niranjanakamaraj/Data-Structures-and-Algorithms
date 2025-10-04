class Node:
    def __init__(self, data):
        self.data = data                                    # Storing the data
        self.next = None                                    # Points to the next node (initially None)

class LinkedList:
    def __init__(self):
        self.head = None                                   
    def insert(self, data):                                 # Inserting a new node at the end of the list
        new_node = Node(data)
        if self.head is None:  
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:                           # Traversing to the last node
                last_node = last_node.next
            last_node.next = new_node                       # Linking the last node to the new node

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current_node = self.head
            while current_node:                             # list Traversal
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")                                   # End of the list

def main():
    linked_list = LinkedList()                              # Creating an empty linked list
    n = int(input("Enter the number of elements you want to insert: "))
    for i in range(n):
        data = int(input(f"Enter element {i+1}: "))
        linked_list.insert(data)
    linked_list.display()

if __name__ == "__main__":
    main()
