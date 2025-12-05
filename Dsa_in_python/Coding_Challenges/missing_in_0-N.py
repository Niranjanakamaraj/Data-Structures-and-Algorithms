xor=len(arr)
for i in range(len(nums)):
    xor^=i^arr[i]
return xor