class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def f(nums):
            cur = nums[:1]
            for i in nums[1:]:
                if len(cur) == 1:
                    if i != cur[0]:
                        cur.append(i)
                else:
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
            return len(cur)

        return f(nums)
