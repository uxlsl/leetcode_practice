class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        change = False
        nums.insert(0,-float('inf'))
        a,b,c = nums[:3]
        for d in nums[3:]:
            if not (b <= c <= d):
                if change:
                    return False
                elif b > c <= d:
                    change = True
                    b = c
                    if a > b:
                        return False
                elif b <= c > d:
                    change = True
                    pre_c = c
                    c = d
                    if b > c:
                        d = pre_c
                else: #a > b > c:
                    return False
            a,b,c = b,c,d
        return True
