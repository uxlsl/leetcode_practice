from solution import Solution, setGuess


def test_solution():
    s = Solution()
    setGuess(10)
    assert s.guessNumber(20) == 10
    setGuess(11)
    assert s.guessNumber(20) == 11
    setGuess(3)
    assert s.guessNumber(20) == 3
