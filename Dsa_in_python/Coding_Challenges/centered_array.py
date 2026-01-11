count=0
for i in range(0,len(nums)):
    sub=[]
    for j in range(i,-1,-1):
        sub.append(nums[j])
        if sum(sub) in sub:
            count+=1
return count