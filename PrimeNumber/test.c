#include <stdio.h>
#include "prime.h"

int main(int argc, char *argv[])
{
    for (int i = -1; i < 65537; ++i)
        if (is_prime_number(i))
            fprintf(stdout, "%d is prime.\n", i);
    
    return 0;
}
