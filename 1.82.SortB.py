# coding: utf-8
# 不需要保持正数序列和负数序列各自原来的顺序，负正交替

def sortB(lists):
    count = len(lists)
    for i in range(0,count):
        if i%2 == 0 and lists[i] < 0:
            continue
        if i%2 == 1 and lists[i] > 0:
            continue
        if i%2 == 0 and lists[i] > 0:
            j = i + 1
            while j < count and lists[j] > 0:
                j = j + 1
            if j == count:
                break
            else:
                lists[i],lists[j] = lists[j],lists[i]
        if i%2 == 1 and lists[i] < 0:
            j = i + 1
            while j < count and lists[j] < 0:
                j = j + 1
            if j == count:
                break
            else:
                lists[i],lists[j] = lists[j],lists[i]
    return lists

print sortB([7, 8, -6, 2, 45, -5])

