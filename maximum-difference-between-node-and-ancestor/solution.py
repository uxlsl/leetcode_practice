# leetcode

class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.maxvalue=0
        self.dfs(root,0,100001)
        return self.maxvalue

    def dfs(self,node,maxv,minv):
        if not node:
            self.maxvalue = max(maxv-minv, self.maxvalue)
        else:
            maxv, minv = max(maxv,node.val), min(minv,node.val)
            self.dfs(node.left,maxv,minv)
            self.dfs(node.right,maxv,minv)

