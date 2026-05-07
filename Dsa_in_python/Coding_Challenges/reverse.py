class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseList(head):
    pre = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = pre
        pre = curr
        curr = nxt
    return pre