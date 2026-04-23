class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseList(head):
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre