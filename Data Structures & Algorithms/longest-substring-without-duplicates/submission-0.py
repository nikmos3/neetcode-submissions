class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        present = {}
        leftWindow = 0

        for i in range(len(s)):
            if s[i] in present:
                leftWindow = max(leftWindow,present[s[i]] + 1)
            present[s[i]] = i
            res = max(res, i-leftWindow + 1)
        return res




        



            

        