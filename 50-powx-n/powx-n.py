class Solution:
    def find_pow(self, x, n):
        if n == 0:
            return 1
        
        a = self.find_pow(x, n // 2)
        
        if n % 2 == 0:
            return a * a
        else:
            return a * a * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.find_pow(x, -n)
        else:
            return self.find_pow(x, n)