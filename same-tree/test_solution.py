from utils import tree, TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    assert s.isSameTree(tree, tree) == True

    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert s.isSameTree(p, q) == True

    p = TreeNode(1, TreeNode(2))
    p = TreeNode(1, None, TreeNode(2))
    assert s.isSameTree(p, q) == False
