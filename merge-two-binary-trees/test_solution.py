from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    tree1 = TreeNode(1,
            TreeNode(3, TreeNode(5)),
            TreeNode(2))
    tree2 = TreeNode(2,
            TreeNode(1,
                None,
                TreeNode(4)),
            TreeNode(3,
                None,
                TreeNode(7)))
    tree3 = s.mergeTrees(tree1, tree2)
    print(tree3)
