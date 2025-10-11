class Solution:
    def gcd(self, a, b):
        gcd=1
        n,p=[],[]
        if a%b==0:
            return b
        elif b%a==0:
            return a
        for i in range(1,int(a**0.5)+1):
            if a%i==0:
                n.append(i)
                n.append(a//i)
        for j in range(1,int(b**0.5)+1):
            if b%j==0:
                p.append(j)
                p.append(b//j)
        for i in range(len(n)):
            for j in range(len(p)):
                if n[i]==p[j] and n[i]>gcd:
                    gcd=n[i]
        return gcd
