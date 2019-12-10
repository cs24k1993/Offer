def FindGreatestSumOfSubArray(lists):
    if lists == None or  len(lists) <= 0:
        return 0
    nCurSum = 0
    nGreatestSum = lists[0]
    for i in range(len(lists)):
        if nCurSum <= 0:
            nCurSum = lists[i]
        else:
            nCurSum = nCurSum + lists[i]
        if nCurSum > nGreatestSum:
            nGreatestSum = nCurSum
    return nGreatestSum

lists = [3,-2,5,2,-7]
print FindGreatestSumOfSubArray(lists)