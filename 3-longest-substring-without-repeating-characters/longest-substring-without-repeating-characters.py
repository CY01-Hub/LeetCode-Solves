class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        answer = 1
        st = set({})
        st.add(s[0])

        i = 0
        j = 1

        while j < n:
            while s[j] in st:
                st.discard(s[i])
                i += 1
            st.add(s[j])
            j += 1
            answer = max(answer, (j-i))

        return answer