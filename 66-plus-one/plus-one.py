class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        ans = []

        for i in digits:
            s += str(i)

        d = int(s) + 1

        for i in str(d):
            ans.append(int(i))
        
        return ans