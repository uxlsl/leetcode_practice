class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def f(nums):
            cur = nums[0:2]
            for i in nums[2:]:
                if cur[-2] > cur[-1]:
                    if cur[-1] < i:
                        cur.append(i)
                    else:
                        cur[-1] = i
                else:
                    if cur[-1] > i:
                        cur.append(i)
                    else:
                        cur[-1] = i
            if len(cur) == 2:
                if cur[0] == cur[1]:
                    return 1
            return len(cur)

        return f(nums)
