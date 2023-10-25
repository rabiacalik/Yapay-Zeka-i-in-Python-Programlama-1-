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
    











































