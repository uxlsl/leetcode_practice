class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        x = None
        y = None
        for i,j in zip(A, B):
            if i != j:
                if x is None:
                    x,y = i,j
                else:
                    if not (x == j and y == i):
                        break
        else:
            if x is None and len(set(A)) == len(A):
                return False
            return True

        return False
