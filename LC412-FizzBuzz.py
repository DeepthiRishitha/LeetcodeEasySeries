class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        output = []
        for el in range(1, n+1):
            if (el % 3 == 0) & (el % 5 ==0):
                output.append("FizzBuzz")
            elif (el % 3 == 0):
                output.append("Fizz")
            elif (el % 5 == 0):
                output.append("Buzz")
            else:
                output.append(str(el))
        return output

s1 = Solution()
s1.fizzBuzz(10)
