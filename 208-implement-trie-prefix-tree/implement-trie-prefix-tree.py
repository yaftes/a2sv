class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.is_end 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True  