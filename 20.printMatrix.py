# coding:utf-8
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
def printMatrix(matrix):
    if matrix == None:
        return
    if matrix == []:
        return []

    printArr = []
    start = 0 # 每次循环起始点
    rows = len(matrix) # 行数
    columns = len(matrix[0]) # 列数

    while rows > 2 * start and columns > 2 * start: # 循环条件
        endX = columns - start - 1
        endY = rows - start - 1

        # 从左到右将数字存入printArr
        for i in range(start,endX+1):
            number = matrix[start][i]
            printArr.append(number)

        # 从上到下将数字存入printArr
        if start < endY:
            for i in range(start+1,endY+1):
                number = matrix[i][endX]
                printArr.append(number)

        # 从右到左将数字存入printArr
        if start < endX and start < endY:
            for i in range(endX-1,start-1,-1):
                number = matrix[endY][i]
                printArr.append(number)

        # 从下到上将数字存入printArr
        if start < endX and start < endY - 1:
            for i in range(endY-1,start,-1):
                number = matrix[i][start]
                printArr.append(number)
        start += 1
    return printArr

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
print printMatrix(matrix)