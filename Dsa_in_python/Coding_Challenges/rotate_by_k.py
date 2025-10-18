def rotateArray(arr: list, k: int) -> list:
    n=len(arr)
    if n<=k:
        k=k%n
    a=arr[:k]
    del arr[:k]
    return arr+a