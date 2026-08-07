class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        return True if number == number[::-1] else False