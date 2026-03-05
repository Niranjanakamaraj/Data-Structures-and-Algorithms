def pw(x,n):
    while n > 0:
    if n % 2 == 1:
        result *= x
    x *= x
    n //= 2