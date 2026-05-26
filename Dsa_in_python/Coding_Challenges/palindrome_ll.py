class Solution(object):
    def isPalindrome(self, head):

        arr = []

        curr = head

        # store linked list values
        while curr:
            arr.append(curr.val)
            curr = curr.next

        l = 0
        r = len(arr) - 1

        # compare from both sides
        while l < r:

            if arr[l] != arr[r]:
                return False

            l += 1
            r -= 1

        return True