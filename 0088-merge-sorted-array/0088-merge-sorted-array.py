import bisect
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:     
        for i in range(len(nums1)-m):
            nums1.pop()
            
        for i in range(n):
            nums1.insert(bisect.bisect_left(nums1,nums2[i]), nums2[i])
            print(nums1)
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        