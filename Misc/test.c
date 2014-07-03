#include <stdio.h>
#include "misc.h"

int main(int argc, char *argv[])
{
    fprintf(stdout, "-1 is power of 2? %d\n", is_power_of_two(-1));
    fprintf(stdout, "0 is power of 2? %d\n", is_power_of_two(0));
    fprintf(stdout, "1 is power of 2? %d\n", is_power_of_two(1));
    fprintf(stdout, "2 is power of 2? %d\n", is_power_of_two(2));
    fprintf(stdout, "3 is power of 2? %d\n", is_power_of_two(3));
    fprintf(stdout, "4 is power of 2? %d\n", is_power_of_two(4));
}