
class Node(object):
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.val = value
        self.pre = pre
        self.next = next

    def __repr__(self):
        return 'Node({}-{})-{}'.format(self.key, self.val,self.next)


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
            if self._head != o:
                p = o.pre
                q = o.next
                if p is not None:
                    p.next = q
                if q is not None:
                    q.pre = p
                tmp = self._head
                self._head = o
                self._head.pre = None
                self._head.next = tmp
                tmp.pre = self._head
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
            if self._head != o:
                p = o.pre
                q = o.next
                if p is not None:
                    p.next = q
                if q is not None:
                    q.pre = p
                    self._head.pre = o
                    self._head,o.next = o,self._head
                    o.pre = None
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
            last = p
            if cur >= self._capacity:
                if last.pre:
                    last.pre.next = None
                del self._dic[last.key]
                if self._head == last:
                    self._head = None
                del last
            new_node = Node(key, value)
            self._dic[key] = new_node
            new_node.next = self._head
            if self._head:
                self._head.pre = new_node
            self._head = new_node
