class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for char in s: 
            if char=="[" or char == '{' or char == '(':
                stack.append(char)
            elif char == ']' or char == '}' or char == ')':
                if not stack:
                    return False 
                
                test = stack.pop()
                if test !=pairs[char]:
                    return False 
        return not stack
                
