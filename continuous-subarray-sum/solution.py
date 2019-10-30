class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        totals = [0]
        total = 0
        for i in nums:
            total += i
            totals.append(total)

        # i为开始,j为结束
        for i in range(len(nums)):
            for j in range(i+2, len(nums)+1):
                #print(nums[i:j])
                #print(totals[j] - totals[i])
                total = totals[j] - totals[i]
                if k == 0 :
                    if total==0:
                        return True
                elif total % k == 0:
                    return True

        return False
