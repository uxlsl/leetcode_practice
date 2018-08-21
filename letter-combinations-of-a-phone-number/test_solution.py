from solution import Solution


def test_solution():
    s = Solution()
    assert sorted(s.letterCombinations('23')) == sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
