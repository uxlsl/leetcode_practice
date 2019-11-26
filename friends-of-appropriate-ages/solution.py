# leetcode
# https://leetcode-cn.com/problems/friends-of-appropriate-ages/


class Solution(object):
    def numFriendRequests1(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = 0
        for a in range(len(ages)):
            for b in range(len(ages)):
                if a == b:
                    continue
                if ages[b] <= 0.5*ages[a] + 7 or ages[b] > ages[a] or (ages[b] > 100 and ages[a] < 100):
                    continue
                count += 1

        return count



class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans
