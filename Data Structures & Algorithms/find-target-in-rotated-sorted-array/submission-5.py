class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0,len(nums) - 1

        while l<=r:
            m = (l+r) // 2

            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] > target or nums[m] < target:     # 1 > 3      r = 1
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

        