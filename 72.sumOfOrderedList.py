# coding:utf-8
'''
对于正整数数组，求最大元素和，要求元素大小必须是升序的
如：data = [5,1,3,4,9,7,6,8]
最大升序序列是：1,3,4,7,8
输入： 5 1 3 4 9 7 6 8
输出：23
'''

if __name__ == "__main__":
    str_lst = input().split()
    length = len(str_lst)
    lst = []
    for i in range(length):
        lst.append(int(str_lst[i]))

    max_value = [0] * length
    global_max = 0
    for i in range(length):
        local_length = len(max_value)
        max = 0
        for j in range(local_length):
            if lst[i] > lst[j] and max < max_value[j]:
                max = max_value[j]
        if max == 0:
            max_value[i] = lst[i]
        else:
            max_value[i] = max + lst[i]
        if max_value[i] > global_max:
            global_max = max_value[i]
    print(global_max)


