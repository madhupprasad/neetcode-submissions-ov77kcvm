from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        opening = set(['(', '{', '['])
        closing = set([')', '}', ']'])
        stack = deque()
        for i in s:
            if i in opening:
                stack.append(i)
            if i in closing:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (i == ']' and top == '[') or (i == ')' and top == '(') or (i == '}' and top == '{'):
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False