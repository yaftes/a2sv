class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_a = []
        stack_b = []
        for char in s:
            if stack_a and char == '#':
                stack_a.pop()
            elif char != '#':
                stack_a.append(char)
        for char in t:
            if stack_b and char == '#':
                stack_b.pop()
            elif char != '#':
                stack_b.append(char)
        return "".join(stack_a) == "".join(stack_b)

        