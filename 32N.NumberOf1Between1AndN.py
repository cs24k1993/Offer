# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones

    def NumberOf1Between1AndN2(self, n):
        ones, m = 0, 1
        while m <= n:
            if ((n // m) % 10) != 0 and ((n // m) % 10) != 1:
                ones += (n // 10 // m + 1) * m
            elif ((n // m) % 10) == 1:
                ones += (n // m // 10) * m + n % m + 1
            m *= 10
        return ones

s = Solution()
print(s.NumberOf1Between1AndN_Solution(15))
print(s.NumberOf1Between1AndN2(526))