#include <limits.h>
#include <stdio.h>
#include "misc.h"

int main(int argc, char *argv[])
{
    for (int i = -1; i < 65537; ++i)
        if (is_power_of_two(i))
            fprintf(stdout, "%d is power of 2.\n", i);
    
    fprintf(stdout, "MAX_LONG = %ld\n", LONG_MAX);
    // fprintf(stdout, "PI with %ld terms of calculations: %f\n", LONG_MAX, calc_PI(1, LONG_MAX));
    
    fprintf(stdout, "0x3F9D70A3H = %f\n", integer_to_float(0xC14570A3)); // -12.34
}