if not nums:
    return 0
l=0
s=set(nums)
for i in s:
    if i-1 not in s:
        count=1
        x=i+1
        while x in s:
            x+=1
            count+=1
        l=max(count,l)
return l