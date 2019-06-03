from solution import Solution


def test_solution():
    s = Solution()
    assert s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
    assert s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") == False
    assert s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") == False
