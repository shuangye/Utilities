/*
gcc -c logic.c
ar -crv libweak.a logic.o weak.o
 */


int WEAK_greet(void);

int WEAK_callGreet(void)
{
	return WEAK_greet();
}
