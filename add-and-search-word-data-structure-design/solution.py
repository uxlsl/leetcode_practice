class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._words = []


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self._words.append(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        for w in self._words:
            if len(w) == len(word):
                for a,b in zip(w, word):
                    if not (b == '.' or a == b):
                        break
                else:
                    return True
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
