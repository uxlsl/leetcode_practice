class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        sums = [0]

        for i in nums:
            total += i
            sums.append(total)

        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sums[j+1] - sums[i] == k:
                    count += 1
        return count


    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # sum[i] - sum[j] = k
        # sum[j] = sum[i] - k
        count = 0
        sum_ = 0
        map_ = {}
        map_[0] = 1

        for i in nums:
            sum_ += i
            count += map_.get(sum_-k,0)
            map_[sum_] = map_.get(sum_, 0) + 1

        return count

