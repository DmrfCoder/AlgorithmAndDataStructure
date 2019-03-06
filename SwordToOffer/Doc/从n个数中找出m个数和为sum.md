# 从n个数中找出m个数和为sum

<center>知识点：</center>


## 题目描述
给定一个长度为m的数组data，从中找出n个，使得n个数的和为sum，如果不存在返回空数组。

## 解题思路
利用递归和回溯的思想，假设我们没有n个数的限制，要找所有的和为sum的序列，我们假设当前已经找到了x个数和为curSum，这x个数对应的下标存在finded这个list中，现在需要找下一个数，那么我们只需要从下标lastValue=finded[-1]+i开始遍历data数组，假设curSum=curSum+lastValue的值小于sum，我们就将lastValue的

## 代码

[这里](../Code/35.py)