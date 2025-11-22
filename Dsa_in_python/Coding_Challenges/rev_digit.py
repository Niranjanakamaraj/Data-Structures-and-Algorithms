class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        n=abs(x)
        while n>0:
            if rev>2**31-1:
                return 0
            rev=rev*10+n%10
            n//=10
        if x<0:
            return -rev
        else:
            return rev