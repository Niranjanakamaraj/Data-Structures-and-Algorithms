class Solution:
    def isPrime(self, n):
        if((n!=2 and n%2==0) or n==1):
            return False
        else:
            arr=[]
            for i in range(3,n):
                if n%i==0:
                    arr.append(i)
                    break
                i=+2
            if len(arr)==0:
                return True
            else:
                return False