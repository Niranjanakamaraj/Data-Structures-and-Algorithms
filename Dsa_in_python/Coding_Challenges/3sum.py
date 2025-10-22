def hasTripletSum(self, arr, target):
    arr.sort()
    for i in range(len(arr)-2):
        k,j=i+1,len(arr)-1
        while i<j :
            if arr[i]+arr[j]+arr[k]==target:
                return True
            elif arr[i]+arr[j]+arr[k]<target:
                k+=1
            else:
                j-=1
    return False