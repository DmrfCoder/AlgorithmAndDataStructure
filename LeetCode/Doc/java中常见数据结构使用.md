# Java中常见数据结构的使用方法

## 队列
```java
Queue<String> queue = new LinkedList<String>();
//添加元素
queue.offer("a");
 //返回第一个元素，并在队列中删除
String first=queue.poll();
queue.element(); //返回第一个元素 
queue.peek(); //返回第一个元素 
        
```
## 栈

Stack<Integer\> st = new Stack<Integer\>();

| 序号 | 方法描述                                                     |
| :--- | :----------------------------------------------------------- |
| 1    | boolean empty()  测试堆栈是否为空。                          |
| 2    | Object peek( ) 查看堆栈顶部的对象，但不从堆栈中移除它。      |
| 3    | Object pop( ) 移除堆栈顶部的对象，并作为此函数的值返回该对象。 |
| 4    | Object push(Object element) 把项压入堆栈顶部。               |
| 5    | int search(Object element) 返回对象在堆栈中的位置，以 1 为基数。 |





