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
                count += 1
                r += 1
            else:
            

            
            
                count -= 1
                seen.remove(s[l])
                l += 1

            max_count = max(max_count,count)
                
                
            
            
            
        return max_count
            

            




                    



        