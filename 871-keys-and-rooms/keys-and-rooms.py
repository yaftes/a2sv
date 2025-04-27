class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        graph = {i:rooms[i] for i in range(len(rooms))}
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        dfs(0)
        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True
        