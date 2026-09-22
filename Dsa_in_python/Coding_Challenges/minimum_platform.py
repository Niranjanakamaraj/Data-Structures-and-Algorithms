def minPlatform(self, arr, dep):
    p=0
    m=p
    arr.sort()
    dep.sort()
    i,j=0,0
    while i<len(arr) and j<len(dep):
        if i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                p+=1
                i+=1
            else:
                p-=1
                j+=1
        m=max(p,m)
    return m