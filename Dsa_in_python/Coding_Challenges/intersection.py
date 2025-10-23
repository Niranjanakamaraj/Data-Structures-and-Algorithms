class Solution:
    def intersectSize(self,a, b):
        c=a+b
        c.sort()
        count=0
        for i in range(1,len(c)):
            if c[i]==c[i-1]:
                count+=1
        return count