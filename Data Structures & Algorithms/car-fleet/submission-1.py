class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position,speed),reverse=True)
        stack = []
        timeT = 0

        for p,s in cars:
            timeT = (target - p)/ s

            if not stack or timeT > stack[-1]:
                stack.append(timeT)

        return len(stack)


        