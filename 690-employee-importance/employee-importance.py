"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph = defaultdict(list)
        values = defaultdict(int)

        for val in employees:

            graph[val.id] = val.subordinates
            values[val.id] = val.importance
        stack = [id]
        visited = set()
        count = values[id]

        while stack:
            node = stack.pop()
            for subord in graph[node]:
                if subord not in visited:
                    count += values[subord]
                    stack.append(subord)
                    visited.add(subord)
        return count




        
        