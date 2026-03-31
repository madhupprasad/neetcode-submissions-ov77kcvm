class Solution:
    def isValid(self, s: str) -> bool:
        pushset = {'(', '{', '['}
        popset = {')', '}', ']'}

        stack = []

        def bracket_match_valid(a,b):
            if a == '}' and b == '{':
                return True
            
            if a == ']' and b == '[':
                return True
            
            if a == ')' and b == '(':
                return True
            
            return False
                

        for i in range(len(s)):
            if s[i] in pushset:
                stack.append(s[i])
            elif s[i] in popset:
                if stack != []:
                    top = stack.pop()
                else:
                    return False
                if not bracket_match_valid(s[i], top):
                    return False
        
        if stack == []:
            return True

        return False