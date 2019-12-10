# coding:utf-8
'''
有一个n面的骰子，掷每一面都是等概率的。其中有m个奖励面，如果掷到奖励面则可以再掷一次骰子。
玩家每掷一次都能获得掷到那一面的分数，求玩家可获得分数的期望。
输入描述：第一行输入两个数 n m 分别表示骰子有 n 面，有 m 个面有奖励（0<=m<n<=10^9）
第二行输入n个数字用空格隔开，表示n个面的分数
输出描述：输出期望，保留小数点后两位

示例：
输入： 6 1
       1 1 1 1 1 1
输出： 1.20
'''

str1 = input().strip().split(' ')
n = float(str1[0])
m = float(str1[1])
str2 = [int(t) for t in input().strip().split(' ')]

everyScore = sum(str2)

score = (everyScore/(1-m/n))/n

print("%.2f" %score)


