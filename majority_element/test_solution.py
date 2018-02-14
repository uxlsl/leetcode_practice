#!-*- coding:utf-8 -*-

from solution import Solution


def test_MajorityElement():
    s = Solution()
    assert s.majorityElement([1]) == 1
    assert s.majorityElement([1,1]) == 1
    assert s.majorityElement([1,1, 1, 1, 2, 2]) == 1

