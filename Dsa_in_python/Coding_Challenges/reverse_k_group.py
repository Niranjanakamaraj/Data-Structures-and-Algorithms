kth = groupPrev

for _ in range(k):
    kth = kth.next

    if not kth:
        return dummy.next