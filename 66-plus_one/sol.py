# Python2
# Question : https://leetcode.com/problems/plus-one/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(str(int("".join(map(str, digits))) + 1))
        return [int(x) for x in digits]
        
