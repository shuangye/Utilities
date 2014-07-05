// calc PI using different algorithms
// algorithm 1: Nilakantha series
// algorithm 2: Gregory–Leibniz series
// Note: use int for terms, and float for return value will greatly
// improve performance, but will decrease accuracy.
double calc_PI(int algorithm, long terms)
{
    double PI;
    
    switch (algorithm) {
    case 1:  // Nilakantha series
        // PI = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4(8*9*10) ...
        PI = 3.0;
        for (long i = 2; i < terms; i += 2) {
            // if (0 == i % 4)
            if (0 == (i & 3))
                PI -= 4.0 / (i * (i + 1) * (i + 2));
            else
                PI += 4.0 / (i * (i + 1) * (i + 2));
        }
        break;
        
    case 2:  // Gregory–Leibniz series        
        // produces 5 correct fractional digits after 500,000 terms
        // PI = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 ...
        PI = 4.0;
        for (long i = 3; i <= terms; i += 2) {
            // (i - 1) % 4 == 0
            if (0 == ((i - 1) & 3))
                PI += 4.0 / i;
            else
                PI -= 4.0 / i;
        }
        
    default:
        PI = -1.0;
        break;
    }   
    
    return PI;
}
