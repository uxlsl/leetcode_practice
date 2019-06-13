class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        record = [False] * (total + 1)
        record[total] = True

        for i in nums:
            for j, v in enumerate(list(record)):
                if v:
                    record[j-i] = True
                for z in range(total//k,total+1,total//k):
                    print(z)
                    if not record[z]:
                        break
                else:
                    return True
            print(i,record)
        return False

