class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # n = len(s)
        # m = len(t)
        # count = 0
        # if n == m:
        #     freq = {}
        #     for i in s:
        #         if i not in freq:
        #             freq[i] = 1
        #         else:
        #             freq[i] += 1
        #     for i in t:
        #         if i not in freq:
        #             return False
        #         else:
        #             freq[i] -= 1
        #     for i in freq.values():
        #         if i != 0:
        #             return False
        #         else:
        #             return True
        # return False

        if len(s)!=len(t):
            return False

        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
                
        return True