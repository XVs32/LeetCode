class Solution:
    
    zero_count = 0
    max_x = 0
    max_y = 0
    path_count = 0
    
    def get_info(self, grid):
        s_x = -1
        s_y = -1
        zero_count = 0
        
        for i in range(self.max_y):
            for j in range(self.max_x):
                if grid[i][j] == 0:
                    zero_count += 1
                elif grid[i][j] == 1:
                    s_x = j
                    s_y = i
        return s_x,s_y,zero_count
    '''Something goes wrong if enter this line'''   
        
    def find_path(self, grid, x, y, count):
        
        '''print ("at" + str(x) + str(y))'''
        
        
        grid[y][x] = -1
        
        if grid[y][x+1] == 0:
            self.find_path(grid,x+1,y,count+1)
        elif grid[y][x+1] == 2 and count == self.zero_count:
            self.path_count += 1
            
        if grid[y][x-1] == 0:
            self.find_path(grid,x-1,y,count+1)
        elif grid[y][x-1] == 2 and count == self.zero_count:
            self.path_count += 1
        
        if grid[y+1][x] == 0:
            self.find_path(grid,x,y+1,count+1)
        elif grid[y+1][x] == 2 and count == self.zero_count:
            self.path_count += 1
            
        if grid[y-1][x] == 0:
            self.find_path(grid,x,y-1,count+1)
        elif grid[y-1][x] == 2 and count == self.zero_count:
            self.path_count += 1
            
        grid[y][x] = 0
            
        return
        
    
    def uniquePathsIII(self, grid) :
        
        self.path_count = 0
        
        self.max_x = len(grid[0])
        self.max_y = len(grid)
        
        for i in range(self.max_y):
            grid[i].insert(0,-1)
            grid[i].append(-1)
        
        bound = [-1 for n in range(self.max_x + 2)]
        grid.insert(0,bound)
        grid.append(bound)
        
        self.max_x += 2
        self.max_y += 2
        
        '''print (grid)'''
        
        s_x, s_y, self.zero_count = self.get_info(grid)
        
        
        
        self.find_path(grid, s_x, s_y, 0)
        return self.path_count
        
a = Solution()
a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
a.uniquePathsIII([[0,1],[2,0]])


