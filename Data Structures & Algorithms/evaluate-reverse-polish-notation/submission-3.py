from collections import deque
import math

class Solution:

    def eval(self, l,r,o):
        l = int(l)
        r = int(r)
        if o == "*":
            return l * r
        elif o == "+":
            return l + r
        elif o == "-":
            return l - r
        elif o == "/":
            return int(float(l) / r)
            


    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["*","/","+","-"])
        stack = deque()
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                r = stack.pop()
                l = stack.pop()
                v = self.eval(l,r,t)
                stack.append(v)
        
        return stack[0]

