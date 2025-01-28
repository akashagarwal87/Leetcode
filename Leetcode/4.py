class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n=len(nums1)
        m=len(nums2)
        pos1=-1
        pos2=-1
        avg=1
        d=(m+n)//2
        if (m+n)%2 == 0:
            pos1=(d-1)
            pos2=d
            avg=2
        else:
            pos1=d
        