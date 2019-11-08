class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        i = 0
        m = [
            (0b11111000, 0b11110000, 3),
            (0b11110000, 0b11100000, 2),
            (0b11100000, 0b11000000, 1),
        ]
        while i < len(data):
            if data[i] & 0b10000000:
                # 多字节
                for flag, value, count in m:
                    if data[i] & flag == value:
                        for _ in range(count):
                            i += 1
                            if i >= len(data):
                                return False

                            if not (data[i] & 0b11000000) == 0b10000000:
                                return False
                        break
                else:
                    return False
            i += 1
        return True
