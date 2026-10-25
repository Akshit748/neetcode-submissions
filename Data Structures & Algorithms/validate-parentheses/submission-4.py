class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2==1:
            return False
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
                
