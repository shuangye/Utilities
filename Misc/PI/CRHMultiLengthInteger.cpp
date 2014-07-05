// CRHMultiLengthInteger.cpp: implementation of the CRHMultiLengthInteger class.
//
//////////////////////////////////////////////////////////////////////

#include "stdafx.h"
#include "pi.h"
#include "CRHMultiLengthInteger.h"

#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif

//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////

CRHMultiLengthInteger::CRHMultiLengthInteger()
{

}

CRHMultiLengthInteger::~CRHMultiLengthInteger()
{

}

//////////////////////////////////////////////////////////////////////

void CRHMultiLengthInteger::addfunc(CRHMultiLengthInteger const *Adelta)
{ CRHMultiLengthInteger *Alv = this;
  int *Ai;
  const int *Ad;
  int j;

    for (j = 0, Ai = &Alv->i[NElements-1], Ad = &Adelta->i[NElements-1]; j < NElements; j++, Ai--, Ad--)
    {
	*Ai += *Ad;
	if (*Ai >= MaxElementValuePlus1)
	{
	    *Ai -= MaxElementValuePlus1;
	    if (Ai <= &Alv->i[0])
		error();	/* overflow */
	    Ai[-1]++;
	}
    }
}

void CRHMultiLengthInteger::subfunc(CRHMultiLengthInteger const *Adelta)
{ CRHMultiLengthInteger *Alv = this;
  int *Ai;
  const int *Ad;
  int j;

    for (j = 0, Ai = &Alv->i[NElements-1], Ad = &Adelta->i[NElements-1]; j < NElements; j++, Ai--, Ad--)
    {
	*Ai -= *Ad;
	if (*Ai < 0)
	{
	    *Ai += MaxElementValuePlus1;
	    if (Ai <= &Alv->i[0])
		error();	/* overflow */
	    Ai[-1]--;
	}
    }
}

void CRHMultiLengthInteger::assign(int const val)
{ CRHMultiLengthInteger *Asuperlong = this;
  int *Ai;

    for (Ai = &Asuperlong->i[0]; Ai < &Asuperlong->i[NElements]; Ai++)
	*Ai = 0;
    Asuperlong->i[0] = val;
}

void CRHMultiLengthInteger::divfunc(unsigned int const divisor)
{ CRHMultiLengthInteger *Alv = this;
  int *Ai;
  __int64 d;

    for (Ai = &Alv->i[0], d = 0; Ai < &Alv->i[NElements]; Ai++)	/* high to low */
    {
	d += *Ai;
	*Ai = d / divisor;
	d = (d % divisor) * MaxElementValuePlus1;
        if (d < 0)
            error();
    }
}

int CRHMultiLengthInteger::compop(CRHMultiLengthInteger const *Ab) const
{ CRHMultiLengthInteger const *Aa = this;
  const int *lAa;
  const int *lAb;

    for (lAa = &Aa->i[0], lAb = &Ab->i[0]; lAa < &Aa->i[NElements]; lAa++, lAb++)   /* high to low */
	if (*lAa != *lAb)
	    return(*lAa - *lAb);
    return(0);
}

void CRHMultiLengthInteger::error() const
{
    printf("\nError\n");
    exit(4);
}

void CRHMultiLengthInteger::operator =(int const val)
{
    assign(val);
}

void CRHMultiLengthInteger::operator /=(unsigned int const divisor)
{
    divfunc(divisor);
}

bool CRHMultiLengthInteger::operator==(CRHMultiLengthInteger const & b) const
{
    return(compop(&b) == 0);
}

bool CRHMultiLengthInteger::operator>(CRHMultiLengthInteger const & b) const
{
    return(compop(&b) > 0);
}

void CRHMultiLengthInteger::operator-=(CRHMultiLengthInteger const & delta)
{
    subfunc(&delta);
}

void CRHMultiLengthInteger::operator+=(CRHMultiLengthInteger const & delta)
{
    addfunc(&delta);
}

CString CRHMultiLengthInteger::ToCString() const
{
    CString s;
    CString p;

    for (int j = 0; j < NElements; j++)
    {
        int k = i[j];

        if (j == 0)
	    p.Format(" %"NDigits"d.", k);
        else
	    p.Format(" %0"NDigits"d", k);

        s += p;

        if ((j % 10) == 0)
            s += "\n";
    }

    return(s);
}

