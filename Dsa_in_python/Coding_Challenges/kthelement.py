class Solution:
    def kthElement(self, a, b, k):
        i,j=0,0
        while k>0:
            if i<len(a) and (j>=len(b) or a[i]<=b[j]) :
                res=a[i]
                i+=1
            else:
                res=b[j]
                j+=1
            k-=1
        return res