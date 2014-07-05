// CRHCalculatePiClass.h: interface for the CRHCalculatePiClass class.
//
//////////////////////////////////////////////////////////////////////

#if !defined(AFX_CRHCALCULATEPICLASS_H__C278968F_10B2_4096_BF1D_C70D071C4EF7__INCLUDED_)
#define AFX_CRHCALCULATEPICLASS_H__C278968F_10B2_4096_BF1D_C70D071C4EF7__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

class CRHCalculatePiClass  
{
public:
	//CRHCalculatePiClass();
	//virtual ~CRHCalculatePiClass();

// vvv CRH

private:
	static void dispresult(void);
	static void do239term(void);
	static void do5term(void);
        static void calculate();
        static void init();

public:
	static void CRHCalculatePi();

// ^^^ CRH
};

#endif // !defined(AFX_CRHCALCULATEPICLASS_H__C278968F_10B2_4096_BF1D_C70D071C4EF7__INCLUDED_)
