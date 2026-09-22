d={}
array=[]
for i in range(len(bulbs)):
    if bulbs[i] in d:
       d[bulbs[i]]+=1
    else:
        d[bulbs[i]]=1
for i in d:
    if d[i]%2!=0:
        array.append(i)
return sorted(array)