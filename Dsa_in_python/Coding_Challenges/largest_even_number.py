num=int(s)
while num>0:
    if (num%10)%2==0:
        return str(num)
        num/=10
return ""