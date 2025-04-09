class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(list)
        trust_counter = defaultdict(int)
        for u,v in trust:
            trusts[u].append(v)
            trust_counter[v] += 1
        
        stack = [1]
        visited = set()

        while stack:
            node = stack.pop()

            if len(trusts[node]) == 0 and trust_counter[node] == n-1:
                return node
            
            for nod in trusts[node]:
                if nod not in visited:
                    stack.append(nod)
                    visited.add(nod)
        return -1

            


        