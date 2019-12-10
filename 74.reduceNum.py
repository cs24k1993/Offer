# coding:utf-8
'''
分解一个数字，为质因数相乘的形式
例如：输入90，打印出90=2*3*3*5
'''
n = int(input())
def reduceNum(n):
    print '{} = '.format(n)  # python 格式化输出    .format和 % 两种形式。另一种 print ('input: %0.2f'  % 3)
    if not isinstance(n, int) or n <= 0 :
        print 'Please input a valid number !'
        exit(0)
    elif n in [1] :
        print '{}'.format(n)
    while n not in [1] :    # 循环保证递归
        for index in xrange(2, n + 1) :
            if n % index == 0:
                n /= index     # let n equal to it n/index
                if n == 1:     # This is the point
                    print index    # The last one
                else :      # index 一定是素数
                    print '{} *'.format(index),
                break
reduceNum(n)
