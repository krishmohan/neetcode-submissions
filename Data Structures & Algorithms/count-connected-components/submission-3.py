class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for edge in edges:
            from_, to = edge[0], edge[1]
            uf.union(from_, to)
        
        # print(uf.connected(0, 1))
        # print(uf.connected(1, 3))

        # print(uf.size(1))
        # print(uf.size(4))

        return uf.count()

class UF:
    def __init__(self, n):
        self._count = n
        self.parent = [i for i in range(n)]
        self._size = [1] * n
    
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self._size[p_root] > self._size[q_root]:
            self.parent[q_root] = p_root
            self._size[p_root] += self._size[q_root]
        else:
            self.parent[p_root] = q_root
            self._size[q_root] += self._size[p_root]

        self._count -= 1

    def connected(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        return p_root == q_root
    
    def count(self):
        return self._count
    
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
        # if self.parent[x] == x:
        #     return self.parent[x]

        # # Path compressed
        # self.parent[x] = self.find(self.parent[x])
        # return self.parent[x]
    
    def size(self, x):
        root = self.find(x)
        return self._size[root]

    