class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop" 
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        result = []
        for word in words:
            w = word.lower()

            if all(char in first_row for char in w):
                result.append(word)
            elif all(char in second_row for char in w):
                result.append(word)
            elif all(char in third_row for char in w):
                result.append(word)

        return result