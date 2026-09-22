def findTwoElement(self, arr):
    a=sum(set(arr))
    b=sum(arr)
    n=len(arr)
    l=(n*(n+1))//2
    return [b-a,l-a]