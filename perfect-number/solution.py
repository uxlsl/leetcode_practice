class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # import itertools
        # i = 2
        # x = num
        # lst = []
        # while i <= x:
            # if x % i == 0:
                # x = x//i
                # lst.append(i)
            # else:
                # i += 1
        # total = set(lst)
        # total.add(1)
        # for i in range(2,len(lst)):
            # for j in itertools.permutations(lst, i):
                # x = j[0]
                # for z in j[1:]:
                    # x *= z
                # total.add(x)
        # return sum(total) == num
        # 关健
        # num = a * b
        if num == 1:
            return False
        count = 1
        k = num
        i = 2
        while(i < k):
            if num % i == 0:
                    count += i + num / i
            k = num / i
            i += 1
        return num == count

