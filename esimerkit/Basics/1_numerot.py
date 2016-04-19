# -*- coding: utf-8 -*-

if __name__ =="__main__":
    # Defining some variables
    # integers
    int_1 = 131
    int_2 = 22
    
    # floats
    float_1 = 42.1
    float_1 = .234
    
    # complex
    complex_1 = 1j
    complex_2 = 11. + 42.2j    
    
    # booleans
    is_true = True
    is_false = False
    
    # Some operations
    sum_int_int = int_1 + int_2
    sum_int_float = int_1 + float_1
    
    multiply_complex_float = complex_2 * float_1
    multiply_complex_complex = complex_1 * complex_2
    complex_pow_two = complex_1 ** 2
    
    boolean_op_1 = is_true == 1
    boolean_op_2 = is_true != is_false
    boolean_op_3 = is_false == 0
    
    # printing results
    print("Sum, integer + integer: %i" % sum_int_int)
    print("Sum, integer + float: %f is float" % sum_int_int)
    print("Mul, complex * float: Real {0.real:.2f} and imag {0.imag:.2f}".format(multiply_complex_float))
    print("Mul, complex * complex: Real {0.real:.2f} and imag {0.imag:.2f}".format(multiply_complex_complex))
    print("Pow, complex ** 2: Real {0.real:.2f} and imag {0.imag:.2f}".format(complex_pow_two))
    print("Boolean operation 1, True == 1: {0}".format(boolean_op_1))
    print("Boolean operation 2, True != False: {0}".format(boolean_op_2))
    print("Boolean operation 3, False == 0: {0}".format(boolean_op_3))