class Solution(object):
    def uniformArray(self, nums1):
        odd = []

        for x in nums1:
            if x % 2 == 1:
                odd.append(x)

        if not odd:
            return True

        mn = min(odd)

        for x in nums1:
            if x % 2 == 0 and x < mn:
                return False

        return True