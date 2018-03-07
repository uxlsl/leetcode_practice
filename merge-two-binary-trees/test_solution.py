from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    tree1 = TreeNode(1)
    tree2 = TreeNode(1)
    print(s.mergeTrees(tree1, tree2))
    assert False
