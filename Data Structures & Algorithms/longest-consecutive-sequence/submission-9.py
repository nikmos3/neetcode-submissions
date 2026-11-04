class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
    
        count = 0

        for num in num_set:
            if num-1 not in num_set:
                

            

                current_num = num
                current_length = 1
                while True:
                    current_num += 1
                    if current_num in num_set:
                        current_length += 1
                    else:
                        break
                    
                count = max(current_length,count)


            
        
        
        return count


        