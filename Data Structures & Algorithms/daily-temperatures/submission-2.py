class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # 38 > 30
                stackt, stackInd = stack.pop() # stack = []
                res[stackInd] = i - stackInd #* res[0] = 1 - 0 = 

            stack.append((t,i)) # (30,0)
        return res



        