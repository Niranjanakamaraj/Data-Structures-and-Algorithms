    def findUnion(a, b):
        n=[]
        l,r,k=0,0,0
        while l<len(a) and r<len(b):
            if a[l]<b[r] :
                v=a[l]
                l+=1
            elif a[l]>b[r]:
                v=b[r]
                r+=1
            else:
                v=a[l]
                l+=1
                r+=1
            if k==0 or n[k-1]!=v:
                n.append(v)
                k+=1
        while l<len(a):
            if k==0 or n[k-1]!=a[l]:
                n.append(a[l])
                k+=1
            l+=1
        while r<len(b):
            if k==0 or n[k-1]!=b[r]:
                n.append(b[r])
                k+=1  
            r+=1
        return n