# -*- coding:utf-8 -*-
import copy


def cmp(x, y):
    if x > y:
        return -1
    else:
        return 0


class Solution:

    def Permutation(self, ss):
        if ss is None:
            return []
        if len(ss) == 0:
            return []
        listss = list(ss)
        listss.sort()
        myList = []
        myList.append(ss)
        self.PermutationHelper(listss, myList)
        return myList

    def PermutationHelper2(self, ss):
        if ss is None:
            return []
        if len(ss) == 0:
            return []
        mylist = []
        mylist.append(ss)
        size = len(ss)
        while True:
            p = len(ss) - 1

            while p >= 1 and ss[p - 1] >= ss[p]:
                p -= 1

            if p == 0:
                break

            q = p
            p -= 1

            while q < size and ss[q] > ss[p]:
                q += 1
            q -= 1

            ss = list(ss)
            t = ss[p]
            ss[p] = ss[q]
            ss[q] = t

            tempss = ss[p + 1:]
            tempss = tempss[::-1]
            ss = ss[0:p + 1] + tempss
            ss = "".join(ss)
            mylist.append(ss)

        return mylist

    def PermutationHelper(self, ss, Mylist):
        size = len(ss)
        for i in range(size - 2, -1, -1):
            if ss[i] < ss[i + 1]:
                flag = 1
                for j in range(size - 1, i, -1):
                    if ss[j] > ss[i]:
                        t = ss[i]
                        ss[i] = ss[j]
                        ss[j] = t

                        tempss = ss[i + 1:]
                        tempss = tempss[::-1]
                        ss = ss[0:i + 1] + tempss
                        flag = 0
                        break
                if flag == 0:
                    Mylist.append("".join(copy.copy(ss)))
                    self.PermutationHelper(ss, Mylist)


def reversedemo(ss):
    return reversed(ss)


def demo():
    ss = "122"
    ss = list(ss)
    mylist = []
    mylist.append(copy.copy(ss))
    s = Solution()
    s.PermutationHelper(ss, mylist)
    for items in mylist:
        print items


# demo()

ss = '122'
s = Solution()
res = s.PermutationHelper2(ss)
for itemRes in res:
    print itemRes
