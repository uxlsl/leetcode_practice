from solution import Solution


def test_solution():
    s = Solution()
    assert s.findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
