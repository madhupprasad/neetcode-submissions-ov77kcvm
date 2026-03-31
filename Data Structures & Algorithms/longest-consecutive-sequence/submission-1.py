class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        longest = 0

        for v in x:
            if (v-1) in x:
                continue
            length = 1
            while (v + length) in x:
                length += 1
            longest = max(length, longest)
        return longest