from solution import Solution


def test_solution():
    s = Solution()
    assert s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC") == "ABC"
