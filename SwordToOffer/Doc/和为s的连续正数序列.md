# 

<center>知识点：</center>


## 题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

## 解题思路
要点1：连续数组的求和公式：s=（a0+an）/2
要点2：设立两个指针p1和p2，初始时p1指向1，p2指向2，然后求解p1到p2范围内的数的和，如果和比待求和大，则p1++，否则p2++，直到最后求出解。

## 代码
```python
    def FindContinuousSequence(self, tsum):
        lowIndex = 1
        highIndex = 2

        res = []
        while highIndex > lowIndex:
            sum = int((highIndex + lowIndex) * (highIndex - lowIndex + 1) / 2)
            if sum == tsum:
                curSqr = range(lowIndex, highIndex+1)
                res.append(curSqr)
                lowIndex += 1

            elif sum < tsum:
                highIndex += 1
            else:
                lowIndex += 1
        return res
```

[这里](../Code/41.py)