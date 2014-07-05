// CRHMultiLengthInteger.h: interface for the CRHMultiLengthInteger class.
//
//////////////////////////////////////////////////////////////////////

#if !defined(AFX_CRHMULTILENGTHINTEGER_H__FDC72436_4839_49AA_88EA_C4D01068AE19__INCLUDED_)
#define AFX_CRHMULTILENGTHINTEGER_H__FDC72436_4839_49AA_88EA_C4D01068AE19__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#define NDecimalPlaces          (1000100)

#define MaxElementValuePlus1    (1000000)
#define NDigits                 "6"
#define NElements               (1 + (NDecimalPlaces+5)/6)

class CRHMultiLengthInteger  
{
public:
	CRHMultiLengthInteger();
	virtual ~CRHMultiLengthInteger();

public:
        void operator =(int const val);
        void operator +=(CRHMultiLengthInteger const & delta);
        void operator -=(CRHMultiLengthInteger const & delta);
        void operator /=(unsigned int const divisor);
        bool operator >(CRHMultiLengthInteger const & b) const;
        bool operator ==(CRHMultiLengthInteger const & b) const;
        CString ToCString() const;

private:
	void assign(int const val);
	void addfunc(CRHMultiLengthInteger const *Adelta);
	void subfunc(CRHMultiLengthInteger const *Adelta);
	int compop(CRHMultiLengthInteger const *Ab) const;
	void divfunc(unsigned divisor);

	void error(void) const;

        int i[NElements];   // [0] is the most significant element
};

#endif // !defined(AFX_CRHMULTILENGTHINTEGER_H__FDC72436_4839_49AA_88EA_C4D01068AE19__INCLUDED_)
