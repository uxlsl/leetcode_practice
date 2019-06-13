class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0

        while i < len(bits):
            if i < len(bits) - 1 and bits[i] == 1 and bits[i + 1] == 0:
                i += 2
            elif i < len(bits) - 1 and bits[i] == 1 and bits[i + 1] == 1:
                i += 2
            elif bits[i] == 0:
                i += 1
                if i == len(bits):
                    return True
            else:
                return False

        return False
