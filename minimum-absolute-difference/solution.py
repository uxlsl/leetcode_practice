class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        arr = sorted(arr)

        l = []

        for i in range(len(arr)-1):
            l.append([arr[i],arr[i+1]])

        l = sorted(l, key=lambda x:abs(x[0]-x[1]))
        ret = [l[0]]

        for i in l[1:]:
            if not abs(i[0]-i[1]) == abs(ret[0][1] - ret[0][0]):
                break
            ret.append(i)

        return ret

