class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False  
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        u = UnionFind(len(points))
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                man = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((man,i,j))
                
        edges.sort()
        min_cost = 0
        count_vertices = 0
        
        for w,a,b in edges:
            if u.find(a) != u.find(b) and count_vertices < len(points) - 1:
                u.union(a,b)
                min_cost += w
            elif count_vertices >= len(points):
                break
        return min_cost
        
        