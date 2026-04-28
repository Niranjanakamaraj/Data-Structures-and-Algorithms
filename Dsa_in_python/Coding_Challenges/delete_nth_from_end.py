class Solution(object):
    def removeNthFromEnd(self, head, n):
        res=ListNode(0)
        count=0
        temp=head
        while temp:
            temp=temp.next
            count+=1
        pos=(count-n)
        if pos==0:
            return head.next
        temp=head
        count=0
        while temp:
            count+=1
            if count==pos:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head