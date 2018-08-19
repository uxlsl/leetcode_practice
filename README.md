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


## 两数之和

给定一个整数数列，找出其中和为特定值的那两个数。

你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]


### 思路
使用记录表!

## 最长公共前缀
编写一个函数来查找字符串数组中最长的公共前缀字符串。

### 思路
使用zip


## 路径总和
给定一棵二叉树和一个总和，确定该树中是否存在根到叶的路径，这条路径的所有值相加等于给定的总和。

例如：
给定下面的二叉树和 总和 = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在总和为 22 的根到叶的路径 5->4->11->2


### 思路
使用递归到每一个节点!



## 二叉树的最小深度

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶节点的最短路径的节点数量。


### 思路
使用递归到每一个叶子节点!


## 根据二叉树创建字符串

你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

示例 1:

输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

输出: "1(2(4))(3)"

解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。
示例 2:

输入: 二叉树: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

输出: "1(2()(4))(3)"

解释: 和第一个示例相似，
除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。

### 思路
观察规律



## Lowest Common Ancestor of a Binary Search Tree


Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.



### 解法

+ 利用bst的特性
+ 二分法



## Find Smallest Letter Greater Than Target

### 解法




如果大于马上返回，没有则返回第一个




## 两整数之和


不使用运算符 + 和-，计算两整数a 、b之和。

示例：
若 a = 1 ，b = 2，返回 3。
1、输入 a，b
2、按照位把ab相加，不考虑进位，结果是 a xor b，即1+1 =0 0+0 = 0 1+0=1，进位的请看下面
3、计算ab的进位的话，只有二者同为1才进位，因此进位可以标示为 (a and b) << 1 ，注意因为是进位，所以需要向左移动1位
4、于是a+b可以看成 （a xor b）+ （(a and b) << 1），这时候如果 (a and b) << 1 不为0，就递归调用这个方式吧，因为（a xor b）+ （(a and b) << 1） 也有可能进位，所以我们需要不断的处理进位。



## 数字转换为十六进制数
知道最高一位做什么就可以
