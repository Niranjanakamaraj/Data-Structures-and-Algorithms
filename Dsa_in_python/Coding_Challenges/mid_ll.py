class Solution(object):
    def middleNode(self, head):
        count=0
        mid=head
        while(mid!=None):
            mid=mid.next
            count+=1
        count=count//2+1
        mid=head
        track=1
        while(mid!=None):
            if(track==count):
                return mid
            else:
                track+=1
                mid=mid.next