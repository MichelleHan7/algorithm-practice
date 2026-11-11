class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        setnums1 = set(nums1)
        setnums2 = set(nums2)
        return list(setnums1 & setnums2)