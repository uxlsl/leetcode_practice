from solution import Solution


def test_solution():
    s = Solution()
    assert s.commonChars(["bella","label","roller"]) == ["e","l","l"]
    assert s.commonChars(["cool","lock","cook"]) == ["c", "o"]
