d={}
a=[]
for i in range(len(nums)):
    if nums[i] in d:
        d[nums[i]]+=1
    else:
        d[nums[i]]=1
    if d[nums[i]] >len(nums)/3 and nums[i] not in a:
        a.append(nums[i])
return a