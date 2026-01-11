count=0
prefix=""
for i in s:
    prefix+=i
    if len(set(prefix))==len(prefix)%3:
        count+=1
return count