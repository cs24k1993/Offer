# coding:utf-8
'''
统计一个数字在排序数组中出现的次数。
思路：（注意判断边缘条件）
1，先找到K的第一个位置（递归）
2，在找到K的第二个位置（递归）
3，相减得出次数
'''
class Solution():
    def getNumberOfK(self,data,k):
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            first = self.getFirstK(data,k,0,length-1)
            last = self.getLastK(data,k,0,length-1)
            if first > -1:  # first返回值为-1时说明data中不存在要查找的k值
                number = last - first + 1
            return number

    def getFirstK(self,data,k,start,end):

        if start > end:     # start应该小于end,并可以判断k的值在data中是否存在(start一直从中间往前移)，如果不存在，返回-1
            return -1
        middleIndex = (start + end) // 2
        middleData = data[middleIndex]

        if middleData == k:
            if middleIndex > 0 and data[middleIndex-1] == k:    # middleIndex的值不能越界，如果第一个元素为查找的元素
                end = middleIndex - 1                           #  则返回第一个元素的位置并作为first
            else:
                return middleIndex
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.getFirstK(data, k, start, end)

    def getLastK(self, data, k, start, end):
        if start > end:
            return -1

        middleIndex = (start + end) // 2
        middleData = data[middleIndex]

        if middleData == k:
            if middleIndex < end and data[middleIndex + 1] == k:    # middleIndex的值不能越界，如果最后一个元素为查找的元素
                start = middleIndex + 1                             #  则返回最后一个元素的位置并作为last
            else:
                return middleIndex
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.getLastK(data, k, start, end)

alist = [3, 3, 3, 3, 4, 5, 5]
s = Solution()
print(s.getNumberOfK(alist, 3))