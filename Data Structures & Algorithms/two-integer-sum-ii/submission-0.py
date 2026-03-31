class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        le = len(numbers)
        r = le - 1
        while numbers[l] + numbers[r] != target:
            curr = numbers[l] + numbers[r]
            if curr < target:
                l+=1
            elif curr > target:
                r-=1
        return [l+1, r+1]