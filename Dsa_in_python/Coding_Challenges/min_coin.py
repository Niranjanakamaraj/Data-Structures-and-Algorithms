class Solution:
    def findMin(self, n):
        coins=[1,2,5,10]
        no=0
        coins.sort(reverse=True)
        i=0
        for i in range(4):
            no+=n//coins[i]
            n%=coins[i]
        return no