#!env python3

"""
# 计算某个数的阶乘末尾有多个少0
# 1 - 10 两数相乘若要产生 0，只有 1 * 10, 2 * 5
# 200! = 1 * 2 * 3 * ... * 199 * 200 可分解为质数因子相乘
# 很明显其中 2 的个数比 5 多，故只要求出 200! 质因子中有多少个 5,
# 就可得到 200! 结尾有多少个连续的 0
# 即 num = [200 / 5] + [200 / 5 / 5] + [200 / 5 / 5 / 5]
# 其中 [x] 表示对 x 取整
# 这种方法不必花高昂的代价求出 n! 也避免了 n! 可能导致的整数溢出
"""

def number_of_trailing_zeros(n):
    num = 0    
    while (n > 0):        
        # num += (n //= 5)
        n //= 5
        num += n
    return num

print("10!: {0}".format(number_of_trailing_zeros(10)))
print("199!: {0}".format(number_of_trailing_zeros(199)))
print("200!: {0}".format(number_of_trailing_zeros(200)))
