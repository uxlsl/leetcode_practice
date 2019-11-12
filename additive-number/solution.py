class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        # 确定前二个数,然后往下搞
        # 累加序列里的数不会以 0 开头，
        # 所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                a, b = num[: i + 1], num[i + 1 : j + 1]
                if len(a) >= 2 and a[0] == "0" or len(b) >= 2 and b[0] == "0":
                    continue
                a, b = int(a), int(b)
                print(a,b)
                count = 2
                k = j + 1
                while k < len(num):
                    c = a + b
                    if not num[k:].startswith(str(c)):
                        break
                    k += len(str(c))
                    a, b = b, c
                    count += 1
                else:
                    if k == len(num) and count > 2:
                        return True
        else:
            return False
