class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        ans = 1
        n = 2

        while n * n <= num:
            if num % n == 0:
                ans += n

                if n != num // n:
                    ans += num // n

            n += 1

        return ans == num