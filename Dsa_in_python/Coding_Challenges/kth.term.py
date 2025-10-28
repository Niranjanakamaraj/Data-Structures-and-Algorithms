class Solution:
    def kthElement(self, a, b, k):
        c=sorted(a+b)
        return c[k-1]