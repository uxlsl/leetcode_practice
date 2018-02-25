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


## 思路

1. 再原有解法上，加多一层
2. 不断修改原来的行
