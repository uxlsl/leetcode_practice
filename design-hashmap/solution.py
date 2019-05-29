class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = 1000
        self.data = [([],[]) for _ in range(self.num)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        i = key % self.num
        x,y = self.data[i]
        try:
            index = x.index(key)
            y[index] = value
        except:
            x.append(key)
            y.append(value)


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        i = key % self.num
        x,y = self.data[i]
        try:
            index = x.index(key)
            return y[index]
        except:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        i = key % self.num
        x,y = self.data[i]
        try:
            index = x.index(key)
            del x[index],y[index]
        except:
            pass

