class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

def delete(head, x):
    if head.data == x:
        return head.next
    t = head
    while t.next:
        if t.next.data == x:
            t.next = t.next.next
            break
        t = t.next
    return head