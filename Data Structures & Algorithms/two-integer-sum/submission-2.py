class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return [seen[nums[i]], i]
            
            present = target - nums[i]
            seen[present] = i


            # {4:0}

    
        