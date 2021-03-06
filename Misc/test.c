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
    
    fprintf(stdout, "0x000061F2 = %f\n", integer_to_float(0x000061F2));
    fprintf(stdout, "0x003C0000 = %f\n", integer_to_float(0x003C0000));
}