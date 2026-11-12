class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = defaultdict(int)
        window_count = defaultdict(int)
        min_length = float('inf')
        l,r = 0,0
        need = 0
        have = 0

        for char in t:
            if char not in count_t:
                need += 1
            count_t[char] += 1


        min_l,min_r = 0,0
        while r < len(s):
            if s[r] in count_t:
                window_count[s[r]] += 1
                if window_count[s[r]] == count_t[s[r]]:
                    have += 1
            r += 1
            while need == have :
                if min_length > r - l + 1:
                    min_length = r - l + 1
                    min_l,min_r = l,r
                if s[l] in window_count:
                    window_count[s[l]] -= 1
                    if window_count[s[l]] < count_t[s[l]]:
                        have -= 1

                
                l += 1

        return s[min_l:min_r] if min_length != float('inf') else ""


                    


                


               

               


            


        