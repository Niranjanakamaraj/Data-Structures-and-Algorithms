def kanades(arr):
    s,m=arr[0],arr[0]
    for i in range(1,len(arr)):
        s+=arr[i]
        if s<arr[i]:
            s=arr[i]
        if s>m:
            m=s
    return m