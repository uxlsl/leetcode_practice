from utils import TreeNode
from solution import Solution


def test_solution():
    s = Solution()
    n = TreeNode(1)
    t = TreeNode(1, n)
    assert s.lowestCommonAncestor(t, t, n) == t

    p = TreeNode(0)
    q = TreeNode(5)
    tree = TreeNode(6,
            TreeNode(2,
                p,
                TreeNode(4,
                    TreeNode(3),
                    q
                    )),
            TreeNode(8,
                TreeNode(7),
                TreeNode(9)))
    assert s.lowestCommonAncestor(tree, p, q).val == 2

