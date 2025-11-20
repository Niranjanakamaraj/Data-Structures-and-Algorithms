def quick_sort(arr,l,r):
    if l<r:
        p=quick(arr,l,r)
        quick_sort(arr,l,p-1)
        quick_sort(arr,p+1,r)
    return arr
def quick(arr,l,r):
    p=arr[l]
    i=l-1
    j=r+1
    while True:
        i+=1
        while arr[i]<p:
            i+=1
        j-=1
        while arr[j]>p:
            j-=1

        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]