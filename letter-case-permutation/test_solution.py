from solution import Solution


def test_solution():
    s = Solution()
    assert s.letterCasePermutation('a1b2') == ["a1b2", "a1B2", "A1b2", "A1B2"]
