def rev(n):
    num=str(n)
    rev=0
    for i in range(len(num)):
        rev=rev*10+(n%10)
        n=n//10
    return rev
n=int(input("Enter a number:"))
print("The reversed number is:",rev(n))