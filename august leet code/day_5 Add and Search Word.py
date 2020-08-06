class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        
        """
        self.words = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        for other in self.words[len(word)]:
            any_mismatch = any(word[x] != '.' and word[x] != other[x] for x in range(len(word)))
            if not any_mismatch:
                return True
        return False
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
