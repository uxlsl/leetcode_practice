# leetcode
# https://leetcode-cn.com/problems/maximum-binary-tree/submissions/
# 按题意做

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def find_max_index(nums, i, j):
            if i > j:
                return -1
            x = i
            for k in range(i+1, j+1):
                if nums[x] < nums[k]:
                    x = k
            return x

        def build(nums, start, end):
            if start > end:
                return None
            i = find_max_index(nums, start, end)
            node = TreeNode(nums[i])
            node.left = build(nums,start, i-1)
            node.right = build(nums,i+1, end)

            return node

        return build(nums, 0, len(nums)-1)
