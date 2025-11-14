def trap(self,arr):
    pre,suf=[],[]
    m,s=0,0
    for i in range(len(arr)):
        if i==0:
            pre.append(arr[i])
        else:
            pre.append(max(pre[i-1],arr[i]))
    for i in range(len(arr)-1,-1,-1):
        if i==len(arr)-1:
            suf.append(arr[len(arr)-1])
        else:
            suf.append(max(suf[-1],arr[i]))
    suf=suf[::-1]
    for i in range(len(arr)):
        m=min(pre[i],suf[i])-arr[i]
        s+=m
    return s