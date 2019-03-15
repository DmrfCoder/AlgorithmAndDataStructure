# -*- coding:utf-8 -*-
'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
'''


class Solution:
    def __init__(self):
        self.array = [-1 for i in range(256)]
        self.index = 0

    # 返回对应char
    def FirstAppearingOnce(self):
        i = 0
        min = -1
        index = 0
        for itemArray in self.array:
            if itemArray != -1 and itemArray != -2:
                if min == -1:
                    min = itemArray
                    index = i
                elif itemArray < min:
                    min = itemArray
                    index = i
            i += 1
        if min == -1:
            return '#'
        return chr(index)

    def Insert(self, char):
        intChar = ord(char)
        if self.array[intChar] > -1:
            self.array[intChar] = -2
        else:
            self.array[intChar] = self.index
            self.index += 1


s = Solution()
s.Insert('g')
print s.FirstAppearingOnce()
s.Insert('o')
print s.FirstAppearingOnce()
s.Insert('o')
print s.FirstAppearingOnce()
s.Insert('g')
print s.FirstAppearingOnce()
s.Insert('l')
print s.FirstAppearingOnce()
s.Insert('e')
print s.FirstAppearingOnce()
