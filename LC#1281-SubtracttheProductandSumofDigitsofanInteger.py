class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        product = 1
        tot = 0
        int_num = [int(digits) for digits in str(n)]
        for digit in int_num:
            product *= digit
            tot += digit
        result = product - tot
        return result