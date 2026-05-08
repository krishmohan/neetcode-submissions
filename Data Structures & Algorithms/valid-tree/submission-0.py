class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF(n)

        for edge in edges:
            from_, to = edge[0], edge[1]
            if uf.connected(from_, to):
                return False
            
            uf.union(from_, to)

        return uf.count() == 1


class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self._count = n

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return
        
        self.parent[q_root] = p_root
        self._count -= 1
    
    def connected(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        return p_root == q_root

    def count(self):
        return self._count

    def find(self, x):
        if self.parent[x] == x:
            return x
        # Path compression
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    