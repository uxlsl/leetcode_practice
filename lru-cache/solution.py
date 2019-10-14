class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__capacity = capacity
        self.__q = []
        self.__dic = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.__dic:
            return -1
        self.__q.remove(key)
        self.__q.insert(0,key)
        return self.__dic[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.__dic:
            self.__q.remove(key)
        if len(self.__q) == self.__capacity:
            k = self.__q.pop()
            del self.__dic[k]
        self.__dic[key] = value
        self.__q.insert(0, key)
