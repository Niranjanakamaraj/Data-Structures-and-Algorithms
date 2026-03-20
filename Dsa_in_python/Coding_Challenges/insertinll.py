class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = {"data": data, "next": self.head}
        self.head = new

    def insert_end(self, data):
        new = {"data": data, "next": None}

        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp["next"]:
            temp = temp["next"]

        temp["next"] = new

    def insert_pos(self, pos, data):
        new = {"data": data, "next": None}

        if pos == 0:
            new["next"] = self.head
            self.head = new
            return

        temp = self.head
        for _ in range(pos - 1):
            if not temp:
                return
            temp = temp["next"]

        if temp:
            new["next"] = temp["next"]
            temp["next"] = new

    def display(self):
        temp = self.head
        while temp:
            print(temp["data"], end=" -> ")
            temp = temp["next"]
        print("None")