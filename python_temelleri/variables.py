# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %% Variables
var1 = 10
var2 = 20

gun = "pazartesi"

#bu sekilde farkli bolumlendirmeler yapabiliyorsun
# %% String

s = "merhabalar efenim.."

# tipini doner
variable_type = type(s)

# uzunlugunu doner
variable_len = len(s)

print(variable_type)
print(variable_len)

# bu sekilde tanımlamalar yapilabiliyor
cevap = '5'*5

# %% Numbers

integer_var = -10

#float - double
double_var = 10.0

# %% Built in Function

#float(10)
#print(kelime)

# %% User Defined Function

i = 10
j = 10

def my_first_function(var_i, var_j):
    """
    bu kisima aciklamalar yazabilirim

    Returns
    -------
    None.

    """
    output = var_i + var_j
    return output

return_output = my_first_function(i, j)

print("sonuc = ", return_output)
    
# %% Default and Flexible Functions

# Default Function
def calculate_circle_perimeter(r, pi = 3.14):
    """
    Parameters
    ----------
    r : int
        çemberin yari capi.
    pi : double, optional
        pi sayisi. The default is 3.14.

    Returns çemberin çevresi
    -------
    output : TYPE
        DESCRIPTION.

    """
    output = 2 * pi * r
    return output

# Flexible Function
def flexible_func(val1, val2, *args):
    print(args)
    output = (val1 + val2) * args[0]
    return output

# flexible_func(1, 2, 5, 6, 7)
# (5, 6, 7)
# Out[31]: 15

# %% Lambda Function

result = lambda x : x*x

print(result(3))








































