
class Node(object):
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.val = value
        self.pre = pre
        self.next = next

    def __repr__(self):
        return 'Node({})-{}'.format(self.val,self.next)


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._dic = {}
        self._capacity = capacity
        self._head = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self._dic:
            o = self._dic[key]
            return o.val
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self._dic:
            o = self._dic[key]
            o.val = value
            p = o.pre
            q = o.next
            if p is not None:
                p.next = q
            if q is not None:
                q.pre = p
            self._head = o
            return

        if self._head is None:
            self._head = Node(key, value)
            self._dic[key] = self._head
        else:
            cur = 1
            p = self._head
            while p.next:
                cur += 1
                p = p.next
            if cur >= self._capacity:
                p.pre.next = None
                del self._dic[p.key]
                del p
            n = Node(key, value)
            n.next = self._head
            self._head.pre = n
            self._head = n
            self._dic[key] = n
