class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binaryS(0,len(nums)-1,nums,target)

    def binaryS(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1

        m = l + ((r-l)//2)

        if target == nums[m]:
            return m
        elif target < nums[m]:
            return self.binaryS(l,m - 1, nums,target)
        else:
            return self.binaryS(m+1,r,nums,target)
