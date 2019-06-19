class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        def same(S,T):
            if len(S) != len(T):
                return False
            a = set(S[i] for i in range(0,len(S),2))
            b = set(T[i] for i in range(0,len(T),2))

            if a != b:
                return False

            a = set(S[i] for i in range(1,len(S),2))
            b = set(T[i] for i in range(1,len(T),2))
            if a != b:
                return False

            return True

        count = 0
        i = 0
        while i < len(A):
            j = i+1
            flag = False
            while j < len(A):
                if same(A[i], A[j]):
                    del A[j]
                else:
                    j += 1
            count += 1
            i += 1

        return count

class Solution(object):
    def numSpecialEquivGroups(self, A):
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})

