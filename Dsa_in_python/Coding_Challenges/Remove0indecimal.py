class Solution(object):
    def removeZeros(self, n):
        a=0
        place=1
        while n>0:
            if n%10!=0:
            a+=n%10*place
            place*=10
        n//=10
        return a