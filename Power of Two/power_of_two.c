bool isPowerOfTwo(int n){
    return !(n & 0x80000000) && n && !(n & (n-1));
}