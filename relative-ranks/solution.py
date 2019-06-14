class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        lst = [(i,v) for i,v in enumerate(nums)]
        lst = sorted(lst,key=lambda x:x[1], reverse=True)
        ret = [0] * len(nums)
        names = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        print(lst)
        for rank,v in enumerate(lst):
            print(rank)
            if rank < len(names):
                ret[v[0]] = names[rank]
            else:
                ret[v[0]] = str(rank+1)

        return ret
