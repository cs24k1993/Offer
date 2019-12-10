class Solution():
    def LeftRotateString(self,str,n):
        if len(str) <= 0 or len(str) < n or n <0:
            return ''
        strList = list(str)
        self.Reverse(strList)
        right = len(strList) - n
        str1 = self.Reverse(strList[:right])
        str2 = self.Reverse(strList[right:])
        resultStr = ''.join(str1) + ''.join(str2)
        return resultStr

    def Reverse(self, list):
        left = 0
        right = len(list) - 1
        while left < right:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
        return list

test = 'abcdefg'
s = Solution()
print(s.LeftRotateString(test, 2))