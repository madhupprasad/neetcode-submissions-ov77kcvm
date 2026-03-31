class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_arr=[]
        for i in range(len(speed)):
            pair_arr.append((position[i], speed[i]))
        pair_arr.sort(key = lambda x:x[0],  reverse=True)

        stack = []

        for p,s in pair_arr:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # we find a fleet
                stack.pop()
        return len(stack)

