class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

        ans, prev_value = 0, 0
        for i in reversed(s):
            curr_value = roman_values[i]
            if curr_value < prev_value:
                ans -= curr_value
            else:
                ans += curr_value
            prev_value = curr_value
    
        return ans