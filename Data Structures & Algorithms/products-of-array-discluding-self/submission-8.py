class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left = [1] * len(nums)
        # right = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     left[i] = nums[i-1] * left[i-1]

        # print(left)

        # for i in range(len(nums)-2,-1,-1):
        #     right[i] = right[i+1] * nums[i + 1]

        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     res[i] = left[i] * right[i]

    

        # return res




        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        right_tracker = 1
        # nums=[1, 1, 2, 8]

        
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * right_tracker
            right_tracker = nums[i] * right_tracker


        return res