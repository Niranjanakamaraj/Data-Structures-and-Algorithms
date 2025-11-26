class Solution:
    def isArmstrong(self, n):
        sum=0
        x=n
        s=str(n)
        while x>0 and n>sum:
            sum+=(x%10)**len(s)
            x//=10
        if n==sum:
            return True
        else:
            return False