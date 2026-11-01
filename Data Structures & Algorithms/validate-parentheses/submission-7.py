class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {')':'(', '}':'{', ']':'['}
        
        stack = []

        for i in range(len(s)):
            if s[i] in charMap and stack and (charMap[s[i]]) == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return True if stack == [] else False
            
            
                