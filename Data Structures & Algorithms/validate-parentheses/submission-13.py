class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(','}':'{',']':'['}
        stack = []

        for i in range(len(s)):
            if stack and s[i] in map:
                if stack[-1] == map[s[i]]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(s[i])
        
    

        return False if stack else True



        