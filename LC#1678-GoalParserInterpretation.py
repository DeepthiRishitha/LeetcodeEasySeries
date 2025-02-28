class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        self.command = command
        if "()" in command:
            command = command.replace("()", "o")
        if "(al)" in command:
            command = command.replace("(al)", "al")
        else:
            command = command
        return command
