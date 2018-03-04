from utils import TreeNode
from solution import Solution


def test_solution():
    tree = TreeNode(5,
            TreeNode(4,
                TreeNode(11,
            TreeNode(7), TreeNode(2))),
                TreeNode(8,
                    TreeNode(13), TreeNode(4, TreeNode(1))))

    print(tree)
    s = Solution()
    assert s.hasPathSum(tree, 22) == False
