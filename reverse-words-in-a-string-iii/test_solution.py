from solution import Solution


def test_solution():
    s = Solution()
    assert s.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
