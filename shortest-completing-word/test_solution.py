from solution import Solution


def test_solution():
    s = Solution()
    assert s.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]) == "pest"
    assert  s.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]) == "steps"
