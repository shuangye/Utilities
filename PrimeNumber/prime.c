#include <math.h>

// �ж�һ����Ȼ���Ƿ�Ϊ����
int is_prime_number (int n)
{
    if (2 > n)
        return 0;
    if (2 == n)
        return 1;
    else {        
        if (0 == n % 2)  // n is an even
            return 0;
        else {  // n is an odd
            for (int i = 3; i < (long long)floor(n / 2); ++i) {
                if (0 == n % i)
                    return 0;
            }
        }
    }
    return 1;
}