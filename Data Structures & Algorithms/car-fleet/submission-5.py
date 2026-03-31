class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        This problem solution requires math creativity.

        1. we can sort the cars based on position.
        2. From last we can calculate the time_taken from the car
        nearest to the target to reach the target.
        3. we can check if the previous car will collide with the car from the stack.
        (if the time_taken is less than the stack car). If it collides remove the last car from stack.
        4. Add new car to stack
        """

        pos_speed_map = {}
        for i in range(len(position)):
            pos_speed_map[position[i]] = speed[i]
        position.sort(reverse = True)
        stack = []
        for p in position:
            stack.append((target-p)/pos_speed_map[p])
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return(len(stack)) 

