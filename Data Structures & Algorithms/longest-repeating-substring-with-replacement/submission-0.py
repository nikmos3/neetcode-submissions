class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        maxFreq = 0
        maxLen = 0
        freqMap = {}

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r],0)
            maxFreq = max(maxFreq, freqMap[s[r]])
            while (r - l + 1) - maxFreq > k:
                freqMap[s[l]] -= 1
                l+=1
            maxLen = max(maxLen, r-l+1) 
        return maxLen
        