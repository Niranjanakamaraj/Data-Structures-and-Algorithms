class Solution:
    def kthElement(self, a, b, k):
        i = j = 0
        while k > 0:
            if i < len(a) and (j >= len(b) or a[i] <= b[j]):
                val = a[i]
                i += 1
            else:
                val = b[j]
                j += 1
            k -= 1
        return val