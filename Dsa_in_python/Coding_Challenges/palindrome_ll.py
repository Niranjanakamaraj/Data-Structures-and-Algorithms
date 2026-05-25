class Solution(object):
    def isPalindrome(self, head):

        arr = []

        curr = head

        # store linked list values
        while curr:
            arr.append(curr.val)
            curr = curr.next

        left = 0
        right = len(arr) - 1

        # compare from both sides
        while left < right:

            if arr[left] != arr[right]:
                return False

            left += 1
            right -= 1

        return True