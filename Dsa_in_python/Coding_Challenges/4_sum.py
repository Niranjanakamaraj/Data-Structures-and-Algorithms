def 4(nums,target):
    nums.sort()
    a=[]
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,len(nums)):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            k,l=j+1,len(nums)-1
            while k<l:
                q=nums[i]+nums[j]+nums[k]+nums[l]
                if q== target:
                    a.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1
                elif q<target:
                    k+=1
                elif q>target:
                    l-=1
        return a