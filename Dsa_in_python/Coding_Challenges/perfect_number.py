class Solution:
    def isPerfect(self, n):
        a=0
        b=n//2+1
        for i in range(1,b):
            if n%i==0:
                a+=i
        if a==n:
            return True
        else:
            return False
        