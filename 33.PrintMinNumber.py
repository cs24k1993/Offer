# -*- coding:utf-8 -*-
'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
# 运行环境Python 3.x
from functools import cmp_to_key
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return ''
        strList = []
        for i in numbers:
            strList.append(str(i))
        # key是一种比较规则
        # 比较 x+y 和 x-y 的大小, 因为为str型, 需要先转换成int型
        key = cmp_to_key(lambda x, y: int(x+y)-int(y+x))
        strList.sort(key=key)
        return ''.join(strList)
    # 使用冒泡排序
    def PrintMinNumber2(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return ''
        strNum = [str(m) for m in numbers]
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if strNum[i] + strNum[j] > strNum[j] + strNum[i]:
                    strNum[i], strNum[j] = strNum[j], strNum[i]
        return ''.join(strNum)

numbers = [5, 3, 8]
s = Solution()
print(s.PrintMinNumber2(numbers))