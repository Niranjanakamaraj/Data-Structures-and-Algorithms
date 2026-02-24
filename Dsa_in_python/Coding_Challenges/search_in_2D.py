if not matrix or not matrix[0]:
    return False
m=len(matrix)
n=len(matrix[0])
l,r=0,m*n-1
while l<=r:
    mid=(l+r)//2
    row=mid//n
    col=mid%n
    element=matrix[row][col]
    if element==target:
        return True
    elif element<target:
        l=mid+1
    else:
        r=mid-1
return False