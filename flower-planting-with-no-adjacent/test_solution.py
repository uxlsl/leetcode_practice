from solution import Solution


def test_solution():
    s = Solution()
    s.gardenNoAdj(4, [[1,2],[3,4]]) == [1,2,3]
    s.gardenNoAdj(N = 3, paths = [[1,2],[2,3],[3,1]]) == [1,2,1,2]
    s.gardenNoAdj(N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]) == [1,2,3,4]
