class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True

        p1, p2 = coordinates[:2]
        if p1[0] - p2[0] != 0:
            k = (p1[1] - p2[1]) / (p1[0] - p2[0])
            b = p1[1] - k * p1[0]

            for i in coordinates[2:]:
                if k * i[0] + b != i[1]:
                    return False

            return True
        else:
            return all(i[0] == p1[0] for i in coordinates[2:])
