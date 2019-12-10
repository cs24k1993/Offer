def FindContinuousSequence(s):
    if s < 3:
        return []

    left, right = 1, 2
    middle = (s + 1) >> 1
    curSum = left + right
    output = []
    while left < middle:
        if curSum == s:
            output.append(range(left,right+1))
            right += 1
            curSum += right
        elif curSum < s:
            right += 1
            curSum += right
        else:
            curSum -= left
            left += 1
    return output

print FindContinuousSequence(15)
