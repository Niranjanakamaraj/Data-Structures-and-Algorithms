d={}
c_s,m=0,0
for i in range(len(nums)):
    c_s+=nums[i]
    if c_s==k:
        m=max(m,i+1)
    if c_s not in d:
        d[c_s]=i
    if c_s-k in d:
        m=max(m,i-d[c_s-k])