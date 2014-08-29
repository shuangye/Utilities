#include "misc.h"

// ref: http://teaching.idallen.com/cst8281/10w/notes/100_ieee754_conversions.txt

// represents a binary or hex as a float point number
float integer_to_float(int target)
{
    float result = 0.0f;
    int sign = 1;  // negative or positive
    int exponent;    
    float mantissa = 1.0f;  // sizeof(float) is assumed to be the same with sizeof(int)
    
    switch(sizeof(target)) {
    case 4:
        // IEEE 754 single precision format is 32 bits, which are (from left to right):
        // One bit for the sign;
        // 8 bits for the exponent and;
        // 23 bits for the mantissa.
    
        // test the most significant bit
        if (0 != (target & 0x80000000))
            sign = -1;

        // the next 8 bits are exponent, with an offset of 127 = (1 << 8 - 1) - 1
        // 0x7F800000 = 01111111 10000000 00000000 00000000
        exponent = ((target & 0x7F800000) >> 23 ) - 127;
        
        // the lowest 23 bits are mantissa
        // 0x00400000 = 00000000 01000000 00000000 00000000
        for (int i = 1, mask = 0x00400000; i < 24; ++i, mask >>= 1) {
            // value * weight            
            mantissa += ((target & mask) >> (23 - i)) * (1.0f / (1 << i));            
        }
        
        #ifdef _DEBUG
        printf("sign = %d, exponent = %d, mantissa = %f\n", sign, exponent, mantissa);
        #endif
        result = sign * (1 << exponent) * mantissa;
        
        break;
        
    case 8:
        // The IEEE 754 double precision format is 64 bits, which are (from left to right):
        // One bit for the sign;
        // 11 bits for the exponent;
        // 52 bits for the mantissa.
    
        if (0 != (target & 0x8000000000000000))
            sign = -1;
            
        // the next 8 bits are exponent, with an offset of 1023?
        exponent = ((target & 0x7F80000000000000) >> 52 ) - 1023;
        
        // the lowest 52 bits are mantissa
        // 0x8000000000000 = 00000000 00001000 00000000 00000000 00000000 00000000 00000000 00000000
        for (int i = 1, mask = 0x8000000000000; i < 53; ++i, mask >>= 1) {
            // value * weight            
            mantissa += ((target & mask) >> (52 - i)) * (1.0f / (1 << i));            
        }
        
        #ifdef _DEBUG
        printf("sign = %d, exponent = %d, mantissa = %f\n", sign, exponent, mantissa);
        #endif
        result = sign * (1 << exponent) * mantissa;
        
        break;
        
    default:
        break;
    }
    
    return result;
}


// represents a float point number as an hex integer
int float_to_hex(float target)
{
    int sign = target < 0.0f ? -1 : 1;
    int exponent;
    const int EXPONENT_OFFSET = 127;
    int power;
    float rest = 0.0f;
    int mantissa = 0;
    int result = 0;
    
    switch(sizeof(target)) {
    case 4:
        // convert to positive integer and find the max power of 2
        for (power = (int)target * sign; is_power_of_two(power); --power)
            ;
        rest = target - power;
        
        // calc the exponent
        for (exponent = 0; 0 == power ; ++exponent, power >>= 1)
            ;
        exponent += EXPONENT_OFFSET;
        
        result = sign << 31 + exponent << 23;
        break;
        
    case 8:
        break;
        
    default:
        break;
    }
    
    return result;
}
