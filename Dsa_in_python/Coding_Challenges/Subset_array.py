class Solution:
    def isSubset(self, a, b):
        a_d={}
        b_d={}
        for i in a:
            if i in a_d:
                a_d[i]+=1
            else:
                a_d[i]=1
        for i in b:
            if i not in a_d or a_d[i]==0:
                return False
            a_d[i]-=1
        return True