/*
gcc -c normal.c
ar -crv libnormal.a normal.o
 */


#include <stdio.h>

int WEAK_greet(void)
{
	printf("Normal %s\n", __func__);
	return 0;
}
