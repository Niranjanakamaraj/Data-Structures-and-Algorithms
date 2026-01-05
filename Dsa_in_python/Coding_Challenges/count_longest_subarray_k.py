c_s,count=0,0
a={0:1}
for i in range(len(nums)):
    c_s+=nums[i]
    if c_s-k in a:
        count+=a[c_s-k]
    if c_s in a:
        a[c_s]+=1
    else:
        a[c_s]=1                
return count