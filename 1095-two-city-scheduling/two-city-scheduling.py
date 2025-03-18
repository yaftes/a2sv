class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_cost = 0
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs)
        for i in range(n):
            if i < n // 2:
                total_cost += costs[i][0]
            else:
                total_cost += costs[i][1]
        return total_cost
        