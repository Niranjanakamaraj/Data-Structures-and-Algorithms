def longest(nums):
    c_s,maxi=0,0
    d={}
    for i in range(len(nums)):
        c_s+=nums[i]
        if c_s==0:
            maxi=max(maxi,i+1)
        elif c_s in d:
            maxi=max(maxi,i-d[c_s])
        else:
            d[c_s]=i
    return max