class Solution:
    def isPalindrome(self, n):
        s=n
        rev=0
        while n>0:
            rev=rev*10+n%10
            n=n//10
        if s==rev:
		    return True
		else:
		    return False