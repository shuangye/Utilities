/*

gcc -c main.c

Weak 函数在独立的库中，还是与调用者在同一个库中，不影响链接到 weak 版本，还是 normal 版本。
库出现的顺序决定着链接 weak 版本，还是 normal 版本。

1) weak 函数与调用者在同一个库中：
gcc -o main main.o -L. -lweak -lnormal   # calls the weak version
gcc -o main main.o -L. -lnormal -lweak   # calls the normal version

2) weak 函数与调用者不在同一个库中：
gcc -o main main.o logic.o -L. -lnormal -lweak   # calls the normal version
gcc -o main main.o logic.o -L. -lweak -lnormal  # calls the weak version

 */

#include <stdio.h>

int WEAK_callGreet(void);

int main(int argc, char *argv[])
{
	return WEAK_callGreet();
}
