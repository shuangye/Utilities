#include <stdio.h>
#include "prime.h"

int main(int argc, char *argv[])
{
    fprintf(stdout, "2 is prime? %d\n", is_prime_number(2));
    fprintf(stdout, "3 is prime? %d\n", is_prime_number(3));
    fprintf(stdout, "4 is prime? %d\n", is_prime_number(4));
    fprintf(stdout, "5 is prime? %d\n", is_prime_number(5));
    fprintf(stdout, "7 is prime? %d\n", is_prime_number(7));
    fprintf(stdout, "9 is prime? %d\n", is_prime_number(9));
    fprintf(stdout, "13 is prime? %d\n", is_prime_number(13));
    fprintf(stdout, "99 is prime? %d\n", is_prime_number(99));
    fprintf(stdout, "101 is prime? %d\n", is_prime_number(101));
    fprintf(stdout, "56515323 is prime? %d\n", is_prime_number(56515323));
    
    return 0;
}
