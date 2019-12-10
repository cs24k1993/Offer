def FindNumbersWithSum(list,s):
    if list == None or len(list) <= 0 or list[-1] + list[-2] < s:
        return []

    left = 0
    right = len(list)-1
    while left < right:
        if list[left]+list[right] == s:
            return list[left],list[right]
        elif list[left]+list[right] > s:
            right -= 1
        else:
            left += 1


list = [1,4,7,8,10]
list2 = []
print FindNumbersWithSum(list,15)