def sub(nums,i,seq):
    if i==len(nums):
        print(seq)
        return
    seq.append(nums[i])
    sub(nums,i+1,seq)
    seq.pop()
    sub(nums,i+1,seq)