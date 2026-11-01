class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}

        for i,n in enumerate(nums): # 0 , 4 
            diff = target - n # diff = 10 - 4 = 6

            if diff in present:  # 6 is not in present = {} 
                return [present[diff], i]
            present[n] = i  # present = {4: 0}
            
            '''
            1, 5
            diff = 5
            5 is not present in {4:0}
            present = {4:0, 5:1}


            2,6
            diff = 4
            4 is present in {4:0, 5:1,}
            return 2,0 
            '''




    '''
    target - nums[i] = 6
    '''


            
        