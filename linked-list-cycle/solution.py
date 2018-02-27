
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        f=s=head

        while f !=None and s != None:
            try:
                f = f.next.next
                s = s.next
                if id(f) == id(s):
                    return True
            except AttributeError:
                return False
        return False

