class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if not node:
                return False

            if i == len(word):
                return node.is_end

            char = word[i]

            if char == '.':
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                index = ord(char) - ord('a')
                return dfs(node.children[index], i + 1)

        return dfs(self.root, 0)
