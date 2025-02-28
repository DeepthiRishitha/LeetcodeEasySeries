class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        tot = 0
        for idx in range(len(nums)):
            if idx>0:
                nums[idx] = nums[idx]+nums[idx-1]
        return nums

        