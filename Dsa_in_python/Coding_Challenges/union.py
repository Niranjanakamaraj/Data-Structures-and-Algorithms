class Solution:    
    def findUnion(self, a, b):
        c=a+b
        c.sort()
        r=[c[0]]
        i=1
        while i<len(c):
            if c[i]!=c[i-1]:
                r.append(c[i])
            i+=1
        return r