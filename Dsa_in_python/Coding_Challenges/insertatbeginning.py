def insert_beginning(self, data):
    new = Node(data)
    new.next = self.head
    self.head = new