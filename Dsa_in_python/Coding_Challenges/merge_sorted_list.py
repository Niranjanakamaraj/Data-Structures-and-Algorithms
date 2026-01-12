a=[]
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        a.append(list1[i])
        i+=1
    else:
        a.append(list2[j])
        j+=1
return a