#!/usr/bin/python

import ast
import inspect
import math
print ("Hello, Python!")

def get_g (L, T, th):
    theta = th * math.pi / 180.0
    par = (1 + 1.0 / 4.0 * math.sin(theta/2)**2)
    return ((4.0 * (math.pi ** 2) * L / T ** 2) * par)

if __name__ == "__main__":
    L=0.5
    T=1.443
    th=30

    g = get_g(0.5, 1.443, 30)
    g1 = get_g(0.5-0.05,1.443+0.02,30-5)
    print("g (0.5,1.443,30) = " + str(g))
    print("g (0.5-0.05,1.443+0.02,30-5) = " + str(g1))
    print("delta(g)/g = " + str((g - g1) / g))
    try :
        print("Format 2 params: %s = %s" % ("one","two"))
        g_name = "rg"
        str1 = "Default Parameters are unknown to C: '"
        val = 60
        print ("Default Parameters are unknown to C: '%s = %s'" % (g_name, str(val)))
        arg_name = g_name
        w_str = ("Default Parameters are unknown to C: '%s = %s'" % (arg_name, str(val)))
        print (w_str)
        print ("Default Parameters are unknown to C: '" + g_name + "=")
        print ("Default Parameters are unknown to C: '" + g_name + " = " )#+ str(60) + "'")
        val += 1
#        w_str = ("Default Parameters are unknown to C:")# '%s = %s'" % (arg_name, "60"))
#        print (w_str)
#       w_str += "OK"
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
