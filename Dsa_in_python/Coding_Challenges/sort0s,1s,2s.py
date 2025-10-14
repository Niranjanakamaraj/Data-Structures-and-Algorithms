class Solution:
    def sort012(self, arr):
        a=arr.count(0)
        b=arr.count(1)
        c=arr.count(2)
        arr.clear()
        for i in range(a):
            arr.append(0)
        for i in range(b):
            arr.append(1)
        for i in range(c):
            arr.append(2)  
        return arr