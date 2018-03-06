from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    tree = TreeNode(3,
            TreeNode(9),
            TreeNode(20,
                TreeNode(15),
                TreeNode(7)))
    assert s.isBalanced(tree) == True

    tree = TreeNode(1,
            TreeNode(2,
                TreeNode(3,
                    TreeNode(4),
                    TreeNode(4))),
            TreeNode(2))
    assert s.isBalanced(tree) == False
