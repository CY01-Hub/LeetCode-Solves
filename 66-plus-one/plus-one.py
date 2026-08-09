class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ""
        l = []

        for i in digits:
            n += str(i)

        a = int(n) + 1

        for i in str(a):
            l.append(int(i))
        
        return l
