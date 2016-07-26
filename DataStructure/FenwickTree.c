/* Fenwick tree, or binary index tree */
/*
 * 设 i 为源数组 src 和树状数组 tree 的下标，从 1 开始。
 * i 表示成二进制时末尾有 x 个 0, 则 tree[i] 位于第 x 层，它包含 2^x 个 src 的元素之和（对这几个元素负责）。
 */

#include <stdlib.h>
#include <stdio.h>

#define BIT_INVALID_SUM       (~0)
#define ERROR(format, ...)    fprintf(stderr, (format), ##__VA_ARGS__)
#define INFO(format, ...)     fprintf(stdout, (format), ##__VA_ARGS__)


typedef void* BIT_Handle;

typedef struct
{
	unsigned int  length;
	int          *pSrc;
	int          *pTree;
} BIT_Array;


static inline int lowBit(const int x)
{
	return x & (-x);
}


void BIT_destroy(BIT_Handle handle)
{
	BIT_Array *pArray = (BIT_Array*)handle;
	
	if (NULL == pArray)
	{		
		return;
	}
	
	free(pArray->pSrc);
	pArray->pSrc = NULL;
	free(pArray->pTree);
	pArray->pTree = NULL;
	free(pArray);
	pArray = NULL;
}

BIT_Handle BIT_create(const unsigned int length)
{
	BIT_Array *pArray = NULL;
	size_t memorySize;
	unsigned int i, j;
	
	if (0 == length)
	{
		ERROR("length %u should be >= 1.\n", length);
		return NULL;
	}
	
	pArray = calloc(1, sizeof(*pArray));
	if (NULL == pArray)
	{
		ERROR("Failed to allocate memory.\n");
		return NULL;
	}
	
	/* subscript starts from 1, so the element at [0] is not used */
	pArray->length = length;
	memorySize = (pArray->length + 1) * sizeof(pArray->pSrc[0]);
	pArray->pSrc  = calloc(1, memorySize);
	pArray->pTree = calloc(1, memorySize);
	if (NULL == pArray->pSrc || NULL == pArray->pTree)
	{
		ERROR("Failed to allocate memory for array elements.\n");
		BIT_destroy(pArray);
	}
	
	for (i = 1; i <= pArray->length; ++i)
	{
		pArray->pSrc[i] = i;
	}
	
	for (i = 1; i <= pArray->length; ++i)
	{
		pArray->pTree[i] = pArray->pSrc[i];
		
		/* tree[i] 对 src[i] 之前的 lowBit(i) 个元素负责 */
		for (j = i - 1; j > i - lowBit(i); --j)
		{
			pArray->pTree[i] += pArray->pSrc[j];
		}
	}
	
	return (BIT_Handle)pArray;
}


int BIT_update(BIT_Handle handle, const unsigned int i, const int delta)
{
	BIT_Array *pArray = (BIT_Array*)handle;
	unsigned int j;
	
	if (NULL == pArray)
	{
		ERROR("Invalid array handle %p.\n", handle);
		return -1;
	}
	
	if (i >= pArray->length)
	{
		ERROR("Invalid index %u.\n", i);
		return -1;
	}
	
	pArray->pSrc[i] += delta;
	
	for (j = i; j <= pArray->length; j += lowBit(j))
	{
		pArray->pTree[j] += delta;
	}
	
	return 0;
}


int BIT_sum(BIT_Handle handle, const unsigned int n)
{
	BIT_Array *pArray = (BIT_Array*)handle;
	unsigned int i;
	int sum = 0;
	
	if (NULL == pArray)
	{
		ERROR("Invalid array handle %p.\n", handle);
		return BIT_INVALID_SUM;
	}
	
	if (n > pArray->length)
	{
		ERROR("Invalid n %u, exceeds the array length %u.\n", n, pArray->length);
		return BIT_INVALID_SUM;
	}
	
	/* 
	 * 对于求数列的前n项和，只需找到n以前的所有最大子树，把其根节点的C加起来即可。
	 * 不难发现，这些子树的数目是n在二进制时1的个数，或者说是把n展开成2的幂方和时的项数.
	 * 1. 从下标为 n 的元素处开始往前计算.
	 * 2. i -= lowBit(i) 是因为 pTree[i] 包含了源数组中 lowBit(i) 个元素之和.
	 * 3. 下标从 1 开始，故结束条件是下标达到 0.
	 */
	for (i = n; i > 0; i -= lowBit(i))
	{
		sum += pArray->pTree[i];
	}
	
	return sum;
}


int BIT_sum2(BIT_Handle handle, const unsigned int n)
{
	BIT_Array *pArray = (BIT_Array*)handle;
	unsigned int i;
	int sum = 0;
	
	if (NULL == pArray)
	{
		ERROR("Invalid array handle %p.\n", handle);
		return BIT_INVALID_SUM;
	}
	
	if (n > pArray->length)
	{
		ERROR("Invalid n %u, exceeds the array length %u.\n", n, pArray->length);
		return BIT_INVALID_SUM;
	}
	
	for (i = 1; i <= n; ++i)
	{
		sum += pArray->pSrc[i];
	}
	
	return sum;
}


void BIT_dump(BIT_Handle handle)
{
	BIT_Array *pArray = (BIT_Array*)handle;
	unsigned int i;
	
	if (NULL == pArray)
	{
		ERROR("Invalid array handle %p.\n", handle);
		return;
	}
	
	for (i = 1; i < pArray->length; ++i)
	{
		INFO("%d, ", pArray->pSrc[i]);
	}
	INFO("%d\n", pArray->pSrc[i]);  /* no extra trailing separator */
}


int main(int argc, char *argv[])
{
	const unsigned int length = 100;
	unsigned int i;
	BIT_Handle handle;

	
	handle = BIT_create(length);	
	for (i = 0; i <= length; ++i)
	{
		INFO("Prefix sum %u = %d (%d).\n", i, BIT_sum(handle, i), BIT_sum2(handle, i));
	}
	BIT_dump(handle);
	
	BIT_update(handle, 50, 1);
	for (i = 0; i <= length; ++i)
	{
		INFO("Prefix sum %u = %d (%d).\n", i, BIT_sum(handle, i), BIT_sum2(handle, i));
	}
	BIT_dump(handle);
	
	BIT_destroy(handle);
	
	return 0;
}
