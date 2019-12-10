# coding: utf-8
def atoi(s):
    # 去除前面的空格
    index = 0
    while index < len(s) and s[index] == ' ':
        index += 1
    # 判断是否全是空字符
    if index == len(s):
        return 0

    #判断非法输入的字符？

    # 判断正负号
    sign = 1
    if s[0] == '-':
        sign = -1
        index += 1
    elif s[0] == '+':
        index += 1

    result = 0

    while index < len(s) and '0' <= s[index] <= '9':
        result = 10 * result + int(s[index])
        index += 1

    if sign == -1:
        return -1 * min(result, 2 << 30)
    else:
        return min(result, (2 << 30) - 1)

if __name__ == '__main__':
    s = '  4312'
    print(atoi(s))
    s = '-3243423423423feawe'
    print(atoi(s))