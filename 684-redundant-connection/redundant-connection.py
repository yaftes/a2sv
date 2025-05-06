class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])  
        return self.parent[n]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] == self.rank[root_y]:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        val = UnionFind(len(edges))

        for u,v in edges:
            p_u = val.find(u)
            p_v = val.find(v)
            print(p_u,p_v)
            if p_u == p_v:
                return [u,v]
            else:
                val.union(u,v)
        return []
        
        