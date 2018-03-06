from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    tree = TreeNode(10,
            TreeNode(5,
                TreeNode(3, TreeNode(3), TreeNode(-2))),
            TreeNode(-3, None, TreeNode(11)))

    assert s.pathSum(tree, 8) == 3
