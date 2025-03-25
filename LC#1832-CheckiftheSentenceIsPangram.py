class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        self.sentence = sentence
        unique_chars = set(sentence)
        if len(unique_chars) == 26:
            return True
        else:
            return False
