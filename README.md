# leedcode 

## 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
括号必须以正确的顺序关闭，"()" 和 "()[]{}" 是有效的但是 "(]" 和 "([)]" 不是。

### 思路
使用堆栈方式


## 验证回文字符串 Ⅱ

给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

```

输入: "aba"
输出: True

```

示例 2:

```

输入: "abca"
输出: True

```

解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。


### 思路

从两端开始，直到不相同的，然后删除一个继续


## 帕斯卡三角形

给定 numRows, 生成帕斯卡三角形的前 numRows 行。

例如, 给定 numRows = 5,

返回

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


## 思路
利用公式


## 帕斯卡三角形 II
给定一个索引 k，返回帕斯卡三角形（杨辉三角）的第 k 行。

例如，给定 k = 3，

则返回 [1, 3, 3, 1]。


### 思路

1. 再原有解法上，加多一层
2. 不断修改原来的行


## 合并两个有序数组

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1中，使得 num1 成为一个有序数组。

注意:

你可以假设 nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。在 nums1 和 nums2 中初始化的元素的数量分别是 m 和 n。


### 思路

由于是合并二个有序数组, 假设v1是插入的第个有序数组的第一个位置，v2就肯定在v1后面!


## 最少爬楼梯代价

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].


### 思路
加一思想!



## 删除链表中的元素
删除链表中等于给定值 val 的所有元素。

示例
给定: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
返回: 1 --> 2 --> 3 --> 4 --> 5



### 思路
注意操作链表的顺序


## 翻转链表

反转一个单链表。


### 思路
注意操作链表顺序

## 相交链表

编写一个程序，找到两个单链表相交的起始节点。



例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

### 思路
长度相同的指针相交

## 环形链表


给定一个链表，判断链表中否有环。

补充：
你是否可以不用额外空间解决此题？

### 思路
快慢指针的应用!


## 最小栈

设计一个支持 push，pop，top 操作，并能在常量时间内检索最小元素的栈。

push(x) -- 将元素x推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。


### 思路
http://blog.jobbole.com/106940/


## Third Maximum Number
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).


### 思路
保持三个最大数
参考
https://www.jianshu.com/p/c4840361199e
