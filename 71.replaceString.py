# coding:utf-8
'''
输入：字符串源码，被替换的子串，目标子串
输出：替换后的新字符串
如输入：
this is a chick
is
are
输出：
thare are a chick
'''
while True:
    try:
        raw_str = raw_input()       # python 3输入只有input函数（默认输入的是字符串，如果要用数字，用int()转换）
        change_str = raw_input()
        target_str = raw_input()
        print  raw_str.replace(change_str, target_str  )
    except:
        break


'''
this is a chick
is
are
tharearea chick  # target_str后面加空格，替换后字符间距就可以分开了
'''