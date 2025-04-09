from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
  
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        colors = {i: "W" for i in range(1, n + 1)}

   
        for i in range(1, n + 1):
            if colors[i] == "W":  
                stack = [i]
                colors[i] = "R" 
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if colors[neighbor] == "W":
                            colors[neighbor] = "B" if colors[node] == "R" else "R"
                            stack.append(neighbor)
                        elif colors[neighbor] == colors[node]:  
                            return False
        
        return True




        
        