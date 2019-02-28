# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        size = len(s)
        #存储不同字符
        array1 = []
        #存储不同字符对应的出现次数
        array2 = []
        #存储不同字符第一次出现的下标
        array3=[]


        for i in range(size):
            if s[i] not in array1:
                array1.append(s[i])
                array2.append(1)
                array3.append(i)
            else:
                index = array1.index(s[i])
                array2[index] += 1

        for i in range(len(array2)):
            if array2[i] == 1:
                return array3[i]

        return -1

s=Solution()
print s.FirstNotRepeatingChar('aabbccd')