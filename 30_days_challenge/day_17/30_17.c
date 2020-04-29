#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void dfs(char **grid, int x, int y){
    printf("in %d %d\n",y,x);
    grid[y][x] = '0';
    
    if(grid[y][x+1] == '1'){
        dfs(grid,x+1,y);
    }
    if(grid[y][x-1] == '1'){
        dfs(grid,x-1,y);
    }
    if(grid[y+1][x] == '1'){
        dfs(grid,x,y+1);
    }
    if(grid[y-1][x] == '1'){
        dfs(grid,x,y-1);
    }
    
    return;
}

int numIslands(char** input, int size_y, int* size_x_ptr){
    
    int size_x = *size_x_ptr;
    
    
    char **grid, *y_ptr;
    int i;
    
    grid= (char **)malloc(sizeof(char *)*(size_y+2)+sizeof(char)*(size_x+2)*(size_y+2));
    for (i=0,y_ptr= (char *)(grid+(size_y+2)); i<(size_y+2); i++, y_ptr+=(size_x+2)){
        grid[i]=y_ptr;
    }
    
    memset(&grid[0][0],0,sizeof(char)*(size_x+2)*(size_y+2));
    
    for (i=0; i<size_y; i++){
        memcpy(&grid[i+1][1],&input[i][0],sizeof(char)*size_x);
    }
    
    
    
    int island = 0;
    
    int x = 1,y = 1;
    for(;y<size_y+1;y++){
        for(;x<size_x+1;x++){
            if(grid[y][x] == '1'){
                dfs(grid,x,y);
                island ++;
                
            }
            

        }
    }
    printf("\n%d\n",island);
    return island;
}



int main(){
    
    char **grid, *y_ptr;
    int i;
    int size_y = 4, size_x = 5;
    
    grid = (char **)malloc(sizeof(char *)*size_y+sizeof(char)*size_x*size_y);
    for (i=0,y_ptr= (char *)(grid+size_y); i<size_y; i++, y_ptr+=size_x){
        grid[i]=y_ptr;
    }
    
    memcpy(&grid[0][0],"11110110101100000000",sizeof(char)*size_x*size_y);
    
    numIslands(grid,size_y,&size_x);
    
    return 0;
}











