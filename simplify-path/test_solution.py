from solution import Solution


def test_solution():
    s = Solution()
    assert s.simplifyPath('/home/') == '/home'
    assert s.simplifyPath('/../') == '/'
    assert s.simplifyPath('/home//foo/') == '/home/foo'
    assert s.simplifyPath('/a/./b/../../c/') == '/c'
    assert s.simplifyPath('/a/../../b/../c//.//') == '/c'
    assert s.simplifyPath('/a//b////c/d//././/..') == '/a/b/c'
