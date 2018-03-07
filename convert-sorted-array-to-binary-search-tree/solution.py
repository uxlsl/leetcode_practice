from utils import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def help(nums, l, h):
            m = (l + h) // 2
            node = TreeNode(nums[m])
            if l <= m-1:
                node.left = help(nums, l,  m -1)
            if m + 1 <= h:
                node.right = help(nums, m + 1, h)
            return node

        if nums:
            return help(nums, 0, len(nums)-1)
        else:
            return None
