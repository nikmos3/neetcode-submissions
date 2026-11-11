class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_count = 0
       
        count = 0
        l = 0
        r = 0


        
    
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                
                r += 1

            else:
            
                
                seen.remove(s[l])
                l += 1

            max_count = max(max_count,r - l )
                
                
            
            
            
        return max_count
            

            




                    



        