def arms(n):
    sum=0
    temp=n
    while n>0:
        a=n%10
        sum+=a*a*a
        n=n//10
    if temp==sum:
         return True
    else:
        return False
n=int(input("Enter a number:"))
print(arms(n))