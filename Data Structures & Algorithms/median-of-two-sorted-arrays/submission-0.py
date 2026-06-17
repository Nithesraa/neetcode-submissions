class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        res.sort()
        ans = 0
        l , r = 0 , len(res)-1
        mid = (l+r)//2
        if len(res) % 2 == 0:
            ans = (res[mid] + res[mid+1])/2
        else:
            ans = res[mid]
        return float(ans)