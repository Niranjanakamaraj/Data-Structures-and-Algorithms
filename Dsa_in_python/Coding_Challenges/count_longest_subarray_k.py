p_s,count=0,0
d={0:1}
for i in range(len(nums)):
    p_s+=nums[i]
    if p_s-k in d:
        count+=d[p_s-k]
        if p_s in d:
            d[p_s]+=1
        else:
            d[p_s]=1
return count