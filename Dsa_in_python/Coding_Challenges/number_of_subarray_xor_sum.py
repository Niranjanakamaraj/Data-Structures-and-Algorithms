def xor(nums,k):
    xor,count=0,0
    dict={0:1}
    for i in range(len(nums)):
        xor^=nums[i]
        if xor^k in dict:
            count+=dict[xor^k]
        if xor in dict:
            dict[xor]+=1
        else:
            dict[xor]=1
    return count