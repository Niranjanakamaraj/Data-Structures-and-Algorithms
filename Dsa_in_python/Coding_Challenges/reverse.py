class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    pre = None
    current = head
    while current:
        nxt = current.next
        current.next = pre
        pre = current
        current = nxt
    return pre