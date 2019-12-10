def LastRemainingNumber(n,m):
    if n < 1 or m < 1:
        return -1

    remainIndex = 0
    for i in range(2,n+1):
        remainIndex = (remainIndex + m) % i
    return remainIndex

print LastRemainingNumber(5,3)