class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        for i in string.punctuation:
            s = s.replace(i,"")
        s = s.replace(" ","")

        return s == s[::-1]