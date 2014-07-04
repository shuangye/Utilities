#include <math.h>

// To determine if n is a prime
int is_prime_number (int n)
{
    // 0 and 1 are not primes
    if (2 > n)
        return 0;
    // 2 is the only even prime number
    if (2 == n)
        return 1;
    // All other even numbers are not primes
    if (0 == (n & 1))
        return 0;
        
    // n is an odd here, so there is no need to divide n by an even.
    // The max factor of n is no more than sqrt(n).
    for (int i = 3; i <= (int)ceil(sqrt(n)); i += 2) {
        if (0 == n % i)
            return 0;
    }
    
    return 1;
}