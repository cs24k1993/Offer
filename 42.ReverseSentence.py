class Solution():
    def ReverseSentence(self,str):
        if str == None or len(str) <= 0:
            return ''
        strList = list(str)
        strList = self.Reverse(strList)
        begin = 0
        end = 0
        resultStr = ''
        listTemp = []

        while end < len(str):
            if end == len(str) - 1:
                listTemp.append(self.Reverse(strList[begin:]))
                break
            if strList[begin] == ' ':
                begin += 1
                end += 1
                listTemp.append(' ')
            elif strList[end] == ' ':
                listTemp.append(self.Reverse(strList[begin:end]))
                begin = end
            else:
                end += 1

        for i in listTemp:
            resultStr += ''.join(i)
        return resultStr

    def Reverse(self,list):
        left = 0
        right = len(list)-1
        while left < right:
            list[left],list[right] = list[right],list[left]
            left += 1
            right -= 1
        return list

str = 'I am a student.'
s = Solution()
print(s.ReverseSentence(str))