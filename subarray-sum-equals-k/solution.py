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
        count = 0
        sum_ = 0
        map_ = {}
        map_[0] = 1

        for i in nums:
            sum_ += i
            if sum_ - k in map_:
                count += map_.get(sum_-k)
            map_[sum_] = map_.get(sum_, 0) + 1

        return count

