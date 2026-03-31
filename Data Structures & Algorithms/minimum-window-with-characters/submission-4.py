from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if s == t:
            return s

        if t in s:
            return t
        
        """
        create a counter of t, right pointer check if in counter
        if so, delete from counter, move left pointer to the current 
        right pointer (only the first time) & right pointer++. We are saving the chars as we move,
        unless we find all the chars in counter. if right has reached 
        the last, we stop. if set is emptied, we store the res. we start from the next char 
        """

        left = 0
        right = 0
        counter = Counter(t)
        flag = False
        sol = ""
        temp_str = ""
        while right <= len(s):
            if sum(counter.values()) == 0:
                print(temp_str)
                if(sol == ""):
                    sol = temp_str
                else:
                    sol = temp_str if len(temp_str) < len(sol) else sol
                # reset counter
                # reset right position using left
                # reset flag
                # reset temp_str
                print(left, right)
                right = left+1
                counter = Counter(t)
                flag = False
                temp_str = ""

            if right == len(s):
                break
                
            if s[right] in counter and counter[s[right]] > 0:
                counter[s[right]] -= 1
                if flag == False:
                    flag = True
                    left = right
                temp_str += s[right]
                right+=1
            else:
                if flag == True:
                    temp_str += s[right]
                right+=1

        return sol
        