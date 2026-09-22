a=[]
ind=[]
for i in range(len(nums)):
    if nums[i]>=0:
        a.append(nums[i])
        ind.append(i)
if len(a)<=1:
    return nums
k=k%len(a)
a[:]=a[k:]+a[:k]
for i in range(len(a)):
    nums[ind[i]]=a[i]