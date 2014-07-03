// To determine is a number is the power of 2.
// Return: 0 indicates not, non-zero indicates being.
// Consider the binary form of a power of 2. Its most significant bit is 1, 
// and all other bits are zero.
// The power of 2 minus 1, however, is opposite: all its bits are ones.
// So use logical AND operation to determine.
// E.g., 8 = 1000B, 8 - 1 = 0111B. 1000B & 0111B = 0.
int is_power_of_two (int n)
{
    if (n <= 0)
        return 0;    
    if (0 == (n & (n - 1)))
        return 1;
    return 0;
}