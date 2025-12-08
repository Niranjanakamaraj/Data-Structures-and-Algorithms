def longest(nums,k):
    cal,length,i=0,0,0
    for j in range(i,len(nums)):
        cal+=nums[j]
        if cal==k and length<j-i+1:
            length=j-i+1
        while cal>k and i<=j:
            cal-=nums[i]
            i+=1
    return length