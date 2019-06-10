from solution import Solution


def test_solution():
    s = Solution()
    assert s.wordBreak("leetcode", ["leet", "code"]) == True
    assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert s.wordBreak("applepenapple", ["apple", "pen"])
