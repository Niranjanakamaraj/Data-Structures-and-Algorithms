class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse(head):
    previous = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = previous
        previous = curr
        curr = nxt
    return previous