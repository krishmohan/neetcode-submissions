class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                edges.append((i, j, distance))
        
        # greedy approch, pick the min dist first
        edges.sort(key=lambda x: x[2])
        
        uf = UF(n)
        mst_distance = 0

        for edge in edges:
            from_, to, distance = edge
            if uf.connected(from_, to):
                continue

            mst_distance += distance
            uf.union(from_, to)
        
        return mst_distance


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