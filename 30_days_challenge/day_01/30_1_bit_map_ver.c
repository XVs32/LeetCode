#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int singleNumber(int* nums, int numsSize){
    
    int i, j;
    unsigned int bit_map[32] = {0};
    
    for (i=0;i<numsSize;i++){
        for (j=0;j<32;j++){
            bit_map[j] += (nums[i] >> j & 1);
        }
    }
    
    int ans=0;
    for (j=0;j<32;j++){
        ans += (bit_map[j] % 2 << j);
    }
    
    return ans;
}


int main(){
    
    int num0[] = {2,2,1};
    printf("%d\n",singleNumber(num0,3));
    
    int num1[] = {4,1,2,1,2};
    printf("%d\n",singleNumber(num1,5));
    
    int num2[] = {-1};
    printf("%d\n",singleNumber(num2,1));
    
}