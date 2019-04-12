# sort-list(排序List)

<center>知识点：排序，链表</center>


## 题目描述

Sort a linked list in O(n log n) time using constant space complexity.

使用常量空间在O（n log n）时间复杂度内对链表进行排序。

## 解题思路

首先思考常见排序算法的事件复杂度及空间复杂度（参考：[八大常见排序算法介绍](https://ai-exception.blog.csdn.net/article/details/79053814)）：

| 排序方法     | 时间复杂度                            | 空间复杂度       |
| ------------ | ------------------------------------- | ---------------- |
| 直接插入排序 | $T(n)=O(n^2)$                         | $S(n)=O(1)$      |
| 希尔排序     | $T(n)=O(n^{1.5})$                     | $S(n)=O(1)$      |
| 冒泡排序     | $T(n)=O(n^2)$                         | $S(n)=O(1)$      |
| 快速排序     | $T(n)=O(nlog_2n)$                     | $S(n)=O(log_2n)$ |
| 选择排序     | $S(n)=O(1)$                           | $T(n)=O(n^2)$    |
| 堆排序       | $T(n)=O(nlog_2n)$                     | $S(n)=O(1)$      |
| 归并排序     | $T(n)=O(nlog_2n)$                     | $S(n)=O(n)$      |
| 基数排序     | $T(n)=O(d*n)$ d为排序数中最大数的位数 | $S(n)=O(n)$      |

从上表中可以看出，对数组而言，时间复杂度为$O（nlogn）$的排序算法有：快速排序、堆排序、归并排序。

快速排序和堆排序都对数组中下标的使用较为依赖，相比之下，归并排序更适合链表，再考虑到数组中归并排序的空间复杂度之所以为$O(n)$是因为合并的时候需要用一个辅助数组记录合并后的值以保证原数组中的数字排序不被破坏，而链表可以使用指针保证这一点而不需要额外辅助数组，所以空间复杂度会降为$O(1)$.

综上，使用归并排序可以很好地解决本问题。

大致逻辑：

```
fun listSort(head):
		centerNode=head链表的中间节点
		//分而治之的思想，分别排序后一半链表和前一半链表
		left=listSort(centerNode.next)
		//将centerNode的next置位null，保证同样是head为头结点，现在的链表长度为原来的一半
		right=centerNode.next=null
		listSort(head)
		//合并两个子链表
		return merge(left,right)
```

这里涉及到找链表中间节点的问题，方法是使用两个指针p、q，初始时p指向head，q指向head.next，当q不为null时：

```
p=p.next
q=q.next.next
```

利用两个指针行走速度快慢的不同最终实现找出链表的中间节点，注意处理好空指针异常即可，这个算法称为快慢指针算法。


## 代码

[这里](../src/four/Solution.java)