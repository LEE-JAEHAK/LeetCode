
class Solution(object):
    counter = 0
    def merge_sort(self, arr):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2
        low_arr = self.merge_sort(arr[:mid])
        high_arr = self.merge_sort(arr[mid:])

        merged_arr = []
        l = h = 0
        while l < len(low_arr) and h < len(high_arr):
            if low_arr[l] < high_arr[h]:
                merged_arr.append(low_arr[l])
                l += 1
            else:
                merged_arr.append(high_arr[h])
                h += 1
                Solution.counter += len(low_arr[l:])
                print("log", low_arr)
        merged_arr += low_arr[l:]
        merged_arr += high_arr[h:]
        return merged_arr

    def isIdealPermutation(self, nums):
        cmax = 0
        for i in range(len(nums) - 2):
            cmax = max(cmax, nums[i])
            if cmax > nums[i + 2]:
                return False
        return True
        # loc = 0
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         loc += 1
        # self.merge_sort(nums)
        # print(loc, Solution.counter)
        # return loc == Solution.counter
        """
        :type nums: List[int]
        :rtype: bool
        """