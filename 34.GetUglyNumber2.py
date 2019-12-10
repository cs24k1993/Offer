# -*- coding:utf-8 -*-
# 算法复杂度n^2，如果index的值比较大，需要运算很多次，计算量较大
def isUglyNumber(n):
    while (n%2 == 0):
        n /= 2
    while (n % 3 == 0):
        n /= 3
    while (n % 5 == 0):
        n /= 5
    return True if n == 1 else False

def getUglyNumber(index):
    count = 0
    number = 0
    while count < index:
        number = number + 1
        if isUglyNumber(number):
            count = count + 1
    return number


print getUglyNumber(100)