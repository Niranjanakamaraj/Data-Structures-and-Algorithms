class Solution:
    def isArmstrong(self, n):
        digits = 0
        temp = n
        while temp > 0:
            digits += 1
            temp //= 10
        total = 0
        x = n
        while x > 0:
            total += (x % 10) ** digits
            x //= 10
        return total == n