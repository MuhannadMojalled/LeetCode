class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        rs = ""
        for i in s:
            rs = i + rs
        return str(x) == rs