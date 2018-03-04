from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, TreeNode(7)))
    assert s.findTarget(tree, 9) == True
    assert s.findTarget(tree, 28) == False
