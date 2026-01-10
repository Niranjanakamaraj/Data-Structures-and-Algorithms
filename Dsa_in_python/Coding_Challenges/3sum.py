nums.sort()
a=[]
for i in range(len(nums)):
    if i>0 and nums[i-1]==nums[i]:
        continue
    j,k=i+1,len(nums)-1
    while j<k:
        tri=nums[i]+nums[j]+nums[k]
        if tri<0:
            j+=1
        elif tri==0:
            a.append([nums[i],nums[j],nums[k]])
            j+=1
            k-=1
            while j<k and nums[j]==nums[j-1]:
                j+=1
            while j<k and nums[k]==nums[k+1]:
                k-=1
        else:
            k-=1
return a