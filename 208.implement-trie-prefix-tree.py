class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        l = len(word)
        node = self.root
        for i in range(l):
            if word[i] not in node:
                node[word[i]] = {}
            node = node[word[i]]
        node["leaf"] = True

    def search(self, word: str) -> bool:
        l = len(word)
        node = self.root
        for i in range(l):
            if word[i] not in node:
                return False
            node = node[word[i]]
        if "leaf" in node:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        node = self.root
        for i in range(l):
            if prefix[i] not in node:
                return False
            node = node[prefix[i]]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
