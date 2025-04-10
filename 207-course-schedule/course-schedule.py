class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white = 0 # unvisited
        grey = 1 # visiting
        black = 2 # visited

        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)

        colors = {i:white for i in range(numCourses)}
    
        def has_cycle(node):
            colors[node] = grey

            for ele in graph[node]:
                if colors[ele] == grey:
                    return True
                elif colors[ele] == white:
                    if has_cycle(ele):
                        return True
            colors[node] = black
            return False

        for node in range(numCourses):
            if colors[node] != black:
                if has_cycle(node):
                    return False
        return True
        