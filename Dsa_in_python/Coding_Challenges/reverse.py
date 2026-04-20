class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    previous = None
    current = head
    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    return previous