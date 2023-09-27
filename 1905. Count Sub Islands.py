class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid, i, j, island):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0  # Mark the cell as visited
                island.append((i, j))  # Add the cell to the island
                dfs(grid, i + 1, j, island)
                dfs(grid, i - 1, j, island)
                dfs(grid, i, j + 1, island)
                dfs(grid, i, j - 1, island)

        def is_sub_island(island1, island2):
            # Check if all cells in island2 are also in island1
            for cell in island2:
                if cell not in island1:
                    return False
            return True

        islands1 = []
        islands2 = []

        # Find islands in grid1
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 1:
                    island = []
                    dfs(grid1, i, j, island)
                    islands1.append(island)

        # Find islands in grid2 and count sub-islands
        sub_islands_count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    island = []
                    dfs(grid2, i, j, island)
                    islands2.append(island)

                    # Check if it's a sub-island
                    for island1 in islands1:
                        if is_sub_island(island1, island):
                            sub_islands_count += 1
                            break

        return sub_islands_count
