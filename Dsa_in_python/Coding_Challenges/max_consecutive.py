m,v=0,0
for i in range(len(nums)):
    if nums[i]==1:
        v+=1
        if v>m:
            m=v
        else:
            v=0
    return m