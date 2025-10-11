class Solution:
    def isPerfect(self, n):
        a=0
        b=int(n**0.5)
        for i in range(1,b+1):
            if n%i==0:
                a+=i+(n//i)
        if (a-n)==n:
            return True
        else:
            return False
        