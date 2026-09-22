class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast=head
        count=0
        while count<n:
            fast=fast.next
            count+=1
        if not fast:
            return head.next
        slow=head
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
    return head