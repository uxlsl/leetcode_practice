class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # m = {}
        # for i,v in enumerate(nums):
        # # 这样会出现超时,如果t过大
        # for j in range(t+1):
        # for x in [v-j,v+j]:
        # if x in m:
        # if i - m[x] <=k:
        # return True
        # m[v] = i

        # m = {}
        # for i,v in enumerate(nums):
        # for key,value in m.items():
        # if i - value <= k and abs(v - value) <= t:
        # return True
        # m[v] = i

        # for i in range(len(nums)):
        # for j in range(1,k+1):
        # j = i - j
        # if j < 0:
        # break
        # if abs(nums[i]-nums[j]) <= t:
        # return True

        def getID(x, w):
            return x // w

        if t < 0:
            return False
        d = {}
        w = t+1
        for i in range(len(nums)):
            m = getID(nums[i], w)
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m-1]) < w:
                return True

            if m + 1 in d and abs(nums[i] - d[m+1]) < w:
                return True
            d[m]=nums[i]
            if i >= k:
                del d[getID(nums[i-k],w)]
        return False
