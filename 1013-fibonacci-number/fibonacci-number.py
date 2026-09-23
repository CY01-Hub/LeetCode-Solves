class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        for i in range(n):
            third = first + second
            first = second
            second = third
        return first