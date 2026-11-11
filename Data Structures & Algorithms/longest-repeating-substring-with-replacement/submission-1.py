class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        r = 0
        max_length = 0
        
        while r < len(s):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            r+= 1

            max_length = max(max_length,r - l )

        return max_length



            

        