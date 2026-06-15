class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        streak = 0
        for i in nums:
            if i-1 not in seen:
                n = 1
                while i+n in seen:
                    n+=1
                streak = max(streak,n)
        return streak
        