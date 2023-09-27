class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj_list = defaultdict(list)
        for i in range( len(parent)):
            if parent[i] != -1:
                adj_list[parent[i]].append(i)
                adj_list[i].append(parent[i])
        @cache
        def dfs(node, parent):
            count = 1
            for neigh in adj_list[node]:
                if neigh == parent:
                    continue
                if neigh != parent:
                    count = max(count, 1 + dfs(neigh, node))
            return count

        max(dfs(i,-1) for  i in range(len(parent)))
