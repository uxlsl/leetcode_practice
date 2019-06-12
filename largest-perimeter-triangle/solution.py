class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import itertools
        ret = 0
        for a,b,c in itertools.permutations(A, 3):
            if a < b + c and b < a + c and c < a + b:
                ret = max(ret, a+b+c)

        return ret

    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        A = sorted(A, reverse=True)
        for i in range(0,len(A)):
            a = A[i]
            for j in range(i+1, len(A)):
                b = A[j]
                find = False
                for k in range(j+1,len(A)):
                    c = A[k]
                    if a < b + c and b < a + c and c < a + b:
                        ret = max(ret,a+b+c)
                        find = True
                        break
                if find:
                    break
        return ret

class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        for i in xrange(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
