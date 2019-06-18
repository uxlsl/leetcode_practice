class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        m = defaultdict(list)
        min_i = None
        for i1,v1 in enumerate(list1):
            for i2,v2 in enumerate(list2):
                if v1 == v2:
                    m[i1+i2].append(v1)
                    if min_i is None:
                        min_i = i1+i2
                    else:
                        min_i = min(i1+i2, min_i)

        if min_i is not None:
            return m[min_i]
        else:
            return []
