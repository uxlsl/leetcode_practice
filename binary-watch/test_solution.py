from solution import Solution


def test_solution():
    s = Solution()
    assert set(s.readBinaryWatch(1)) == set(["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"])
