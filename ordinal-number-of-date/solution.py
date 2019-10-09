class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        import datetime

        year, month, day = [int(i) for i in date.split("-")]
        a = datetime.date(year, 1, 1)
        b = datetime.date(year, month, day)
        return (b - a).days + 1
