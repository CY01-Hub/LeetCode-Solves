class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        count = {}

        for word in words:
            for w in word:
                if w not in count:
                    count[w] = 1
                else:
                    count[w] += 1
        
        for c in count:
            if count[c] % len(words) != 0:
                return False
        
        return True
            