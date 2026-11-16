class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        map = {0:1}
        total = 0
        count = 0

        for i in range(len(nums)):
            total += nums[i]
            
            if (total - k) in map:
                count += map[total-k]

            if total in map:
                map[total] += 1
            else:
                map[total] = 1
        return count

            


        

        