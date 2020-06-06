# Python2
# Question : https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # using custom sort function
        # sort the list based on the heights of people in desc order,
        # in case, people have same heights, sort based on K param
        # Eg lambda x: (-x[0], x[1])
        # - sign denotes the desc order, + sign shows the asc order
        # when the custom sort function requires more than One param, pass in parenthesis ()
        people = sorted(people, key = lambda p: (-p[0], p[1]))
        sp = []
        for i in range(len(people)):
          sp.insert(people[i][1], people[i])
        return sp
