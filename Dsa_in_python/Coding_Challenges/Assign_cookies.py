class Solution(object):
    def findContentChildren(self, g, s):
        count=0
        s.sort()
        g.sort()
        i,j=0,0
        while i<len(s) and j<len(g):
            if s[i] >=g [j] :
                count+=1
                i+=1
                j+=1
            else:
                i+=1
        return count