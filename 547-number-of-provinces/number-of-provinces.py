class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i != j:
                    graph[i+1].append(j+1)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        count = 0

        for i in range(1,len(isConnected)+1):
            if i not in visited:
                dfs(i)
                count += 1
        return count

        
        



        