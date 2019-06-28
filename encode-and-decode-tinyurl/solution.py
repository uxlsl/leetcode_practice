class Codec:

    def __init__(self):
        self.id = 0
        self.m1 = {}
        self.m2 = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.m1:
            return self.m1[longUrl]
        tinyurl = 'http://tinyurl.com/{}'.format(self.id)
        self.m1[longUrl] = tinyurl
        self.m2[tinyurl] = longUrl
        self.id += 1
        return tinyurl


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.m2[shortUrl]
