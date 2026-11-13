class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        _min = 1001


        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] > nums[l]:
                r = mid - 1
                
            else:
                _min = min(_min,nums[mid])
                r = mid - 1
                

        return _min
                

        