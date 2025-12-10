i,k,j=0,0,len(nums)
while k<=j:
    if nums[k]==0:
        nums[i],nums[k]=nums[k],nums[i]
        i+=1
        k+=1
    elif nums[k]==1:
        k+=1
    else:
        nums[k],nums[j]=nums[j],nums[k]
        j-=1
return nums