class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        if len(nums) == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        for i in range(0,len(nums),2):
            if i+1 >= len(nums):
                return nums[i]
            if nums[i] == nums[i+1]:
                continue
            else:
                return nums[i]
            i += 1