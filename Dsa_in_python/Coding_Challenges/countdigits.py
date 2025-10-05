def count_digits(n):
    count=0
    num=str(n)
    for i in num:
        count+=1 
    return count
n=int(input("Enter a number:"))
print("The number contains",count_digits(n),"digits")