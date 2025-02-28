class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        split_string_list = list(s)
        for idx,el in enumerate(split_string_list):
            if el == "I":
                split_string_list[idx] = 1
            if el == "V":
                split_string_list[idx] = 5
            if el == "X":
                split_string_list[idx] = 10
            if el == "L":
                split_string_list[idx] = 50
            if el == "C":
                split_string_list[idx] = 100
            if el == "D":
                split_string_list[idx] = 500
            if el == "M":
                split_string_list[idx] = 1000
            tot = 0
        for idx, val in enumerate(split_string_list):
            if idx == len(split_string_list)-1:
                tot = tot + val
            elif val >= split_string_list[idx+1]:
                tot = tot + val
            else:
                tot = tot - val
        return tot

s1=Solution()
s1.romanToInt('III')

        