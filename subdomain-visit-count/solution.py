class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        m = defaultdict(int)
        for s in cpdomains:
            count, domain = s.split()
            count = int(count)
            m[domain] += count
            index = -1
            while True:
                index = s.find('.', index+1)
                if index == -1:
                    break
                m[s[index+1:]] += count
        return ['{} {}'.format(v,k) for k,v in m.items()]
