class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = num < 0
        num = abs(num)

        result = ""

        while num != 0:
            result += str(num % 7)
            num = num // 7

        result = result[::-1]

        if neg:
            result = "-" + result
        
        return result