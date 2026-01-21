def xor(nums):
    c_xr,maxi=0,0
    d={}
    for i in range(len(nums)):
        c_xr^=nums[i]
        if c_xr==0:
            maxi=max(maxi,i+1)
        elif c_xr in d:
            maxi=max(maxi,i-d[c_xr])
        else:
            d[c_xr]=i
    return maxi