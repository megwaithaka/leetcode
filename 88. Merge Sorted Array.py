class Solution(object):
    
    def merge(self, nums1, m, nums2, n):
        
        len(nums1) == m + n
        len(nums2) == n
        0 <= m, n <= 200
        1 <= m + n <= 200
        #-109 <= nums1[i], nums2[j] <= 109
        
        nums1.extend(nums2)
        return nums1.sort()
