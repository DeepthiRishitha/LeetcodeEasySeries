class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        res = nums + nums
        return res