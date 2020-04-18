class Solution:
    
    tem_grid = [[]]
    
    def clear_island(self,grid, x ,y):
        grid[x][y] = "0"
        if grid[x-1][y] == "1":
            self.clear_island(grid, x-1 ,y)
        if grid[x+1][y] == "1":
            self.clear_island(grid, x+1 ,y)
        if grid[x][y-1] == "1":
            self.clear_island(grid, x ,y-1)
        if grid[x][y+1] == "1":
            self.clear_island(grid, x ,y+1)
        
        return
    
    def numIslands(self, grid):

        self.tem_grid = grid;
        
        if not grid:
            return 0
        
        row_size = len(self.tem_grid)
        col_size = len(self.tem_grid[0])

        i = 0
        for i in range(row_size):
            self.tem_grid[i].insert(0, 0)
            self.tem_grid[i].append(0)
        col_size += 2
        
        self.tem_grid.insert(0, [0]*col_size)
        self.tem_grid.append([0]*col_size)
        row_size += 2
        print(self.tem_grid)

        island = 0
        flag = True
        while flag == True:
            
            flag = False
            
            for i in range(row_size):
                for j in range(col_size):
                    if self.tem_grid[i][j] == "1":
                        self.clear_island(self.tem_grid,i,j);
                        print("")
                        print(self.tem_grid)
                        island += 1
                        flag = True
            
        return island
    
a = Solution()

print (a.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print (a.numIslands([[]]))
print (a.numIslands([]))
print (a.numIslands([["1","1","1"],["0","1","0"],["0","1","0"]]))