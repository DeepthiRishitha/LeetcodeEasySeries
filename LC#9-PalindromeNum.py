class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = x
        if x<0:
            return False
        x = list(str(x))
        if(x == list(reversed(x))):
            return True
        return False
        
        
