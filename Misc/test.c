#include <stdio.h>
#include "misc.h"

int main(int argc, char *argv[])
{
    for (int i = -1; i < 65537; ++i)
        if (is_power_of_two(i))
            fprintf(stdout, "%d is power of 2.\n", i);
}