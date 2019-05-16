"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if len(employees) == 0:
            return 0
        info = {}
        for employee in employees:
            info[employee[0]] = employee

        score = 0
        stack = [id]

        while stack:
            id = stack.pop(0)
            score  += info[id][1]
            stack += info[id][2]

        return score

