class Solution(object):
    def intersect(self, nums1, nums2):
        return list((Counter(nums1) & Counter(nums2)).elements())
        