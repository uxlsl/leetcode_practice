from solution import Solution


def test_solution():
    s = Solution()
    letters = ["c", "f", "j"]
    target = 'a'
    assert s.nextGreatestLetter(letters, target) == 'c'
    target = 'c'
    assert s.nextGreatestLetter(letters, target) == 'f'
    target = 'd'
    assert s.nextGreatestLetter(letters, target) == 'f'
    target = 'g'
    assert s.nextGreatestLetter(letters, target) == 'j'
    target = 'j'
    assert s.nextGreatestLetter(letters, target) == 'c'
    target = 'k'
    assert s.nextGreatestLetter(letters, target) == 'c'
