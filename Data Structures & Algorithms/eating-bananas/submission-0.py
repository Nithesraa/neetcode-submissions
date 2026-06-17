from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        ans = r
        while l <= r:
            mid = (l+r)//2
            hr = 0
            for p in piles:
                hr += ceil(p/mid)
            if hr <= h:
                r = mid -1
                ans = mid
            else:
                l = mid + 1
        return ans