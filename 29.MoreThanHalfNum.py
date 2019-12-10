def MoreThanHalfNum(lists):
    n = len(lists)
    if lists == None or n <= 0:
        return 0
    result  = lists[0]
    times = 1
    for i in range(1,n):
        if times == 0:
            result = lists[i]
            times = 1
        elif lists[i] == result:
            times = times + 1
        else:
            times = times - 1
    return result

lists = [1,1,2,2,1,2,2,5,5,5,5,5,5]
print MoreThanHalfNum(lists)