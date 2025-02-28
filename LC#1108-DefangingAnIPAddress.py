class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        self.address = address
        if "." in address:
            address = address.replace(".", "[.]")
        return address
    