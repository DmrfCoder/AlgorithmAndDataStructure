# -*- coding:utf-8 -*-

def quickSort(data, low, high):
    if low >= high:
        return

    partitionIndex = partition(data, low, high)
    quickSort(data, low, partitionIndex - 1)
    quickSort(data, partitionIndex + 1, high)


def partition(data, low, high):
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


#a = [7, 4, 6, 3, 22, 9, 10, 2]
#quickSort(a, 0, len(a) - 1)
#print a
a=input("")
print a