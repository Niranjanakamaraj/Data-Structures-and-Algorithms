def print_to_number(n,i=1):
    if i>n:
        return
    print(i)
    print_to_number(n,i+1)