ind=-1
        ans=float('inf')
        for i,a in enumerate(capacity):
            if a==itemSize :
                return i
            if a>itemSize and a<ans:
                ans=a
                ind=i
        return ind©leetcode