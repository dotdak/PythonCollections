import copy
class Trie:
    def __init__(self, end=False):
        self.key = {}
        self.end = end
    def insert(self, s):
        pointer = self
        for i in range(len(s)):
            if pointer.key.get(s[i]) is None:
                pointer.key[s[i]] = Trie()
            pointer = pointer.key[s[i]]
        pointer.end = True
    def __repr__(self):
         return 'Trie(key={}, {})'.format(list(self.key.keys()), self.end)
        
def wordBreak(s, wordDict):
    def breakRcs(s, ans, word, node):
        if not s:
            ans.append(word)
        i = 0
        _pointer = node
        while i < len(s) and s[i] in _pointer.key:
            if _pointer.end and i > 0:
                breakRcs(s[i:], ans, '{} {}'.format(word, s[:i]) if word else s[:i], node)
            _pointer = _pointer.key[s[i]]
            i += 1
        if _pointer.end:
            breakRcs(s[i:], ans, '{} {}'.format(word, s[:i]) if word else s[:i], node)
    
    trie = Trie()
    for word in wordDict:
        trie.insert(word)
    ans = []
    breakRcs(s, ans, '', trie)
    return ans

if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(wordBreak(s, wordDict)) 
    trie = Trie()
    for word in wordDict:
        trie.insert(word)

