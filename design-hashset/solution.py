class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = 1000
        self.data = [[] for _ in range(self.num)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        x = key % self.num
        if key not in self.data[x]:
            self.data[x].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            x = key % self.num
            self.data[x].remove(key)


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        x = key % self.num
        return key in self.data[x]
