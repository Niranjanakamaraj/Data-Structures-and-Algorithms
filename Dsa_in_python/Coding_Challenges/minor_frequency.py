f=[0]*128
        for a in s:
            f[ord(a)]+=1
        v=set()
        count=0
        for a in s:
            if a in v:
                continue
            if 'a'<=a<='z':
                mirror=chr(ord('a')+ord('z')-ord(a))
            else:
                mirror=chr(ord('0')+ord('9')-ord(a))
            count+=abs(f[ord(a)]-f[ord(mirror)])
            v.add(a)
            v.add(mirror)
        return count©leetcode