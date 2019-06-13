from solution import Solution


def test_solution():
    s = Solution()
    assert s.wordBreak("catsanddog",wordDict = ["cat", "cats", "and", "sand", "dog"]) == [
             "cats and dog",
             "cat sand dog"
             ]
