class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        temporary = x
        reverse = 0
        while temporary > 0:
            remender = temporary % 10
            reverse = (reverse * 10) + remender
            temporary = temporary // 10
        
        if reverse == x:
            return True
        else:
            return False
