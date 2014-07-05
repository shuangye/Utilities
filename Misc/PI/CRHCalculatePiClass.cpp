// CRHCalculatePiClass.cpp: implementation of the CRHCalculatePiClass class.
//
//////////////////////////////////////////////////////////////////////

#include "stdafx.h"
#include "pi.h"
#include "CRHCalculatePiClass.h"

#ifdef _DEBUG
#undef THIS_FILE
static char THIS_FILE[]=__FILE__;
#define new DEBUG_NEW
#endif

//////////////////////////////////////////////////////////////////////

#include <sys\timeb.h>

#include "CRHMultiLengthInteger.h"

CRHMultiLengthInteger answer;
CRHMultiLengthInteger zero;
CRHMultiLengthInteger term5;
CRHMultiLengthInteger term239;
CRHMultiLengthInteger term5m;
CRHMultiLengthInteger term239m;
int n5;
int n239;

CStdioFile ResultFile;

//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////

unsigned long ftimediff(struct timeb *pTimeA, struct timeb *pTimeB)
{
    return((1000 * pTimeA->time + pTimeA->millitm)
         - (1000 * pTimeB->time + pTimeB->millitm));
}

void CRHCalculatePiClass::CRHCalculatePi()
{
    struct timeb StartTime, EndTime;
    ftime(&StartTime);

    init();
    calculate();

    ftime(&EndTime);

    CString Filename;
    Filename.Format("result%i.txt", NDecimalPlaces);
    ResultFile.Open(Filename, CFile::modeCreate | CFile::modeWrite | CFile::modeNoInherit | CFile::shareExclusive);
    ResultFile.WriteString(" pi is approximately" "\n\n");
    dispresult();

    unsigned long NMilliseconds = ftimediff(&EndTime, &StartTime);
    CString TimeInfo;
    TimeInfo.Format("\n\n" " Time taken is %i.%03i seconds", NMilliseconds / 1000, NMilliseconds % 1000);
    ResultFile.WriteString(TimeInfo);
}

void CRHCalculatePiClass::init(void)
{
    term5 = 16;     
    term5 /= 5;     
    n5 = 0;

    term239 = 4;    
    term239 /= 239; 
    n239 = 0;

    answer = 0;     
    zero = 0;       
}

void CRHCalculatePiClass::calculate(void)
{
    for (;;)
    {
	do5term();
        if (term5m == zero)
            break;
    }

    for (;;)
    {
	do239term();
        if (term239m == zero)
            break;
    }
}

void CRHCalculatePiClass::do5term()
{
    term5m = term5;
    term5m /= n5 * 2 + 1; 
    if (n5 % 2 == 0)
	answer += term5m;  /* n5 is even */
    else	
        answer -= term5m;  /* n5 is odd */
    term5 /= 5 * 5;     
    n5++;
}

void CRHCalculatePiClass::do239term()
{
    term239m = term239;
    term239m /= n239 * 2 + 1;   
    if (n239 % 2 == 0)
	answer -= term239m;  /* n239 is even */
    else	
        answer += term239m;  /* n239 is odd */
    term239 /= 239 * 239;     
    n239++;
}

void CRHCalculatePiClass::dispresult()
{
    CString r = answer.ToCString();
    ResultFile.WriteString(r);
}
