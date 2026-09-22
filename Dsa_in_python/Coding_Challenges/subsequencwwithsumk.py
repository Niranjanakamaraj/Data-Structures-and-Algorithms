def subsequencesum(nums,i,seq,s):
    if i==len(nums):
        if s==k:
            print(seq)
        return
    seq.append(nums[i])
    subsequencesum(nums,i+1,seq,s+nums[i])
    seq.pop()
    subsequencesum(nums,i+1,seq,s)