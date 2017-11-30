#def Iq(q, porod_scale, porod_exp, lorentz_scale, lorentz_length, peak_pos, lorentz_exp):
#    z = abs(q - peak_pos) * lorentz_length
#    inten = (porod_scale / q ** porod_exp
#                + lorentz_scale / (1 + z ** lorentz_exp))
#    return inten

# algorithm
# 1. identfy function name
# 2. identify parameters
# 3. identify statements (by indentations)
# 4. determine tokens in statements to be either Parameters, Local Variables or Functions.

import re
print ("Hello, Python!")
file_lines = list()
line = list ()
data_file = open ("a.py", "r")
print ("File opened")
file_lines = data_file.readlines()
print ("File Lines:")
print (file_lines)
print ("----------:")
data_len = len(file_lines)
src = file_lines[0];
src.replace ("(", " (")
line = src.split()

file_text = data_file.read()
print (file_text)
print ("# of charachters: %d", len (file_text))
print ("# of charachters: %d", data_len)
data_file.close ()
print ("File closed")
