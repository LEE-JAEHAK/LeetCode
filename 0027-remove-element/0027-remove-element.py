class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [i for i in nums if i != val]
        return len(nums)