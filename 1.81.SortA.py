# -*- coding: utf-8 -*-
'''
给一个包含正负整数的数组，要求对这个数组中的数进行重新排列，使得其正负交替出现。
首先出现负数，然后是正数，然后是负数。有多余的一方，就放在末尾。
[1,2,3,-4]->[-4,1,2,3]         [1,-3,2,-4,-5]->[-3,1,-4,2,-5]
要求:使用O(1)的空间
问1：如果需要保持正数序列和负数序列各自原来的顺序，如何做，时间复杂度是多少？
问2：如果不需要保持正数序列和负数序列各自原来的顺序，如何做，时间复杂度是多少？
'''
# 不改变正数序列和负数序列各自原来的顺序，负正交替

def posNeg(lists):
    count = len(lists)
    for i in range(0,count):
        if i%2 == 0 and lists[i] < 0:
            continue
        if i%2 == 1 and lists[i] > 0:
            continue
        if i%2 == 0 and lists[i] > 0:
            j = i     # 是不是 j = i + 1 就可以?
            while j < count and lists[j] > 0:
                j = j + 1
            if j == count:
                break
            else:
                for k in range(j,i,-1):
                    if k - i == 1:
                        lists[k-1], lists[k] = lists[k], lists[k-1]
                        break
                    else:
                        lists[k-1], lists[k] = lists[k], lists[k-1]
                        continue
        if i%2 == 1 and lists[i] < 0:
            j = i
            while j < count and lists[j] < 0:
                j = j + 1
            if j == count:
                break
            else:
                for k in range(j,i,-1):
                    if k - i  == 1:
                        lists[k-1], lists[k] = lists[k], lists[k-1]
                        break
                    else:
                        lists[k-1], lists[k] = lists[k], lists[k-1]
                        continue

    return lists

lists = [7,6,8,-1,2,3,-5]
print posNeg(lists)