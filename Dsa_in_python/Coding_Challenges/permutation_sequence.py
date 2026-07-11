class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr=[]
        for i in range(n):
            arr.append(i+1)
        fact=1
        k=k-1
        for i in range(1,n):
            fact*=i
        def f(k,fact):
            if len(arr)==1:
                return str(arr[0])
            i=k//fact
            take=arr.pop(i)
            k%=fact
            if len(arr):
                fact//=len(arr)
            return str(take)+f(k,fact)
        return f(k,fact)