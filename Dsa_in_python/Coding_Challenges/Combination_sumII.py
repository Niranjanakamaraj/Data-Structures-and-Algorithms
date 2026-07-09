subset,r=[],[]
        candidates.sort()
        def f(i,target):
            if target==0:
                r.append(subset.copy())
                return
            elif target<0:
                return 
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                subset.append(candidates[j])
                f(j+1,target-candidates[j])
                subset.pop()
        f(0,target)
        return r