class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char != ']':
                if num != 0:
                    stack.append(num)
                num = 0
                stack.append(char)
            else:
                current = ""
                while stack and stack[-1] != '[':
                    current = stack.pop() + current
                if len(stack) > 1:
                    stack.pop()
                    stack.append(current * stack.pop())
        return "".join(stack)



       
    
        
    
        
            
        