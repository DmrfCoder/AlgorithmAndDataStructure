# -*-coding:utf-8
import copy


def FindC(data, n, findedList, s, finded, curS):
    """
    从data数组中找出n个数使其和为s，可能的数组组合可能不止一个

    :param data: 数组，必须需要从小到大排过序
    :param n: 一共找n个元素
    :param findedList:item是finded，记录所有的可能的组合
    :param s:和为s
    :param finded: 当前可能数组组合中元素对应的下标
    :param curS:当前finded元素中的和，用它记录起来就不用每次都计算sum（finded）的值了

    """
    if n == 0:
        return
        # 开始下标，如果finded中有元素就应该是finded的最后一个元素
    startIndex = 0
    if len(finded) != 0:
        startIndex = finded[-1] + 1
    # 从startIndex向后遍历data
    for i in range(startIndex, m):
        # 假设data[i]是组合中的一个数
        curS += data[i]
        # 如果加上data[i]之后curS的值还是小于s
        if curS < s:
            # 先将i加入finded
            finded.append(i)
            # 利用递归从data中找下一个元素
            FindC(data, n, findedList, s, finded, curS)
            # 回溯，消除刚才的i，因为i不一定是最终组合的数，消除其影响后方便下一次遍历
            curS -= data[i]
            del finded[-1]
        # 如果curS等于s而且元素数列为n-1（因为finded中没append i，所以只用等于n-1即可）
        elif curS == s and len(finded) == n - 1:
            findedValue = []
            for itemFinded in finded:
                findedValue.append(data[itemFinded])
            findedValue.append(data[i])
            findedList.append(findedValue)
            break
        else:
            break


def quickSort(data, low, high):
    if low>=high:
        return
    centerIndex = partation(data, low, high)
    quickSort(data, low, centerIndex - 1)
    quickSort(data, centerIndex + 1, high)


def partation(data, low, high):
    curValue = data[low]
    while low < high:
        while low < high and data[high] >= curValue:
            high -= 1

        t = data[low]
        data[low] = data[high]
        data[high] = t

        while low < high and data[low] <= curValue:
            low += 1

        t = data[low]
        data[low] = data[high]
        data[high] = t

    return low


data = [4, 2, 1, 4, 6, 3]
quickSort(data,0,len(data)-1)
print data
# findedList = []
# finded = []
# curS = 0
# m = 6
# s = 12
# n = 4
# FindC(data, n, findedList, s, finded, curS)
# print findedList
