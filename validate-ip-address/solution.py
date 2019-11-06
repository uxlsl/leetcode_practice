class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        def isIpv4(ip):
            s = ip.split(".")
            if len(s) != 4:
                return False
            for i in s:
                if i == "" or len(i) != 1 and i[0] == "0":
                    return False
                if not i.isdigit():
                    return False
                if not 0 <= int(i) <= 255:
                    return False
            return True

        def isIpv6(ip):
            s = ip.split(":")
            h = set("0123456789abcdef")
            if len(s) != 8:
                return False
            for i in s:
                if i == "" or len(i) > 4:
                    return False
                for j in i:
                    if j.lower() not in h:
                        return False
            return True

        if isIpv4(IP):
            return "IPv4"
        elif isIpv6(IP):
            return "IPv6"
        else:
            return "Neither"
