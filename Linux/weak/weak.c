/*
gcc -c weak.c
ar -crv libweak.a weak.o
 */


#include <stdio.h>

__attribute__((weak))
int WEAK_greet(void)
{
	printf("Weak %s\n", __func__);
	return 0;
}
