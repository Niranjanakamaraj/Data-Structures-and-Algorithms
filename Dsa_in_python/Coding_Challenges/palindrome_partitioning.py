class Solution:
    def palinParts (self, s):
        ans,path=[],[]
        l,r=0,len(s)
        def p(s,l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def f(i):
            if i==len(s):
                ans.append(path.copy())
            for j in range(i,len(s)):
                if p(s,i,j):
                    path.append(s[i:j+1])
                    f(j+1)
                    path.pop()
        f(0)
        return ans