from solution import Solution

# 示例 1:
# 输出："IDID"
# 输出：[0,4,1,3,2]
# 示例 2：

# 输出："III"
# 输出：[0,1,2,3]
# 示例 3：

# 输出："DDI"
# 输出：[3,2,0,1]

def test_solution():
    s = Solution()
    assert s.diStringMatch("IDID") == [0,4,1,3,2]
    assert s.diStringMatch("III") == [0,1,3,2]
    assert s.diStringMatch("DDI") == [3,2,0,1]
