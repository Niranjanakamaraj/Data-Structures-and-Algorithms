count1,count2=0,0
a,b=float('-inf'),float('-inf')
for i in range(len(nums)):
    if count1==0 and nums[i]!=a:
        a=nums[i]
        count1=1
    elif count2==0 and nums[i]!=b:
        b=nums[i]
        count2=1
    elif nums[i]==a:
        count1+=1
    elif nums[i]==b:
        count2+=1
    else:
        count1-=1
        count2-=1
r=[]
if nums.count(a)>len(nums)//3:
    r.append(a)
elif b!=a and nums.count(b)>len(nums)//3:
    r.append(b)
return r