def inversionCount(self, arr):
        count=0
        l,r=0,len(arr)-1
        def divide(arr,l,r):
            if l>=r:
                return
            m=(r+l)//2
            divide(arr,l,m)
            divide(arr,m+1,r)
            mergesort(arr,l,m,r)
        def mergesort(arr,l,m,r):
            nonlocal count
            left=arr[l:m+1]
            right=arr[m+1:r+1]
            i,j,k=0,0,l
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    arr[k]=left[i]
                    i+=1
                else:
                    arr[k]=right[j]
                    j+=1
                    count+=len(left)-i
                k+=1
            while i<len(left):
                arr[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
        divide(arr,l,r)
        return count