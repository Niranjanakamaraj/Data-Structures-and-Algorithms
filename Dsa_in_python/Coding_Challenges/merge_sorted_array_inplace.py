def merge(nums1,m,nums2,n):
    a,c,b=m-1,n-1,len(nums1)-1
    while c>=0:
        if a>=0 and nums1[a]>nums2[c]:
            nums1[b]=nums1[a]
            a-=1
        else:
            nums1[b]=nums2[c]
            c-=1
        b-=1