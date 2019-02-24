# 包含min函数的栈

<center>知识点：栈</center>


## 题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
## 解题思路
使用两个数组，第一个数组用来实现栈先入后出的功能（记为数组A），第二个栈实现存储当前栈最小值的功能（记为数组B），具体做法是，每来
一个待入栈的元素，将其先入数组A，然后将其与数组B的最后一个元素即B栈的栈顶比较，如果当前元素比B栈栈顶小，则将其入B栈，否则将B栈的倒数第一个再入一次栈，弹栈时A和B同时弹，这样可以保证B栈的当前栈顶一定是A栈中的最小元素，而且避免了弹栈时A和B栈元素个数不一样的情况。
举个例子：元素为[7,3,4,8,7,1,10],那么A个B栈的元素应该是：
A：[7,3,4,8,7,1,10]
B：[7,3,3,3,3,1,1]
这样弹栈顺序和对应时刻min值为：
弹栈：10，1，7，8，4，3，7
min：1，1，3，3，3，3，7
## 代码
```python
class Solution:
    def __init__(self):
        self.a = []
        self.b = []
        self.count = 0

    def push(self, node):
        # write code here
        if self.count == 0:
            self.b.append(node)
            self.count += 1

        elif node < self.b[-1]:
            self.b.append(node)
            self.count += 1
        else:
            self.b.append(self.b[-1])
            self.count += 1
        self.a.append(node)

    def pop(self):
        # write code here
        r = self.a[-1]
        self.a.pop()
        self.b.pop()
        self.count -= 1
        return r

    def top(self):
        # write code here
        return self.a[-1]

    def min(self):
        # write code here
        return self.b[-1]

```
[这里](../Code/19.py)