from solution import Solution


def test_solution():
    s = Solution()
    assert s.isIsomorphic('egg' ,'add') == True
    assert s.isIsomorphic('foo' ,'bar') == False
    assert s.isIsomorphic('paper' ,'title') == True
