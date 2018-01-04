import sys
import sys
import math
import numpy as np

#==== polymer_excl_volume ====
def Iq6(q, rg=60.0, porod_exp=3.0):
    usub = (q*rg)**2 * (2.0/porod_exp + 1.0) * (2.0/porod_exp + 2.0)/6.0
    if q <= 0:
        result = 1.0
    else:
        upow = power(usub, -0.5*porod_exp)
        result= (porod_exp*upow *
                (gamma(0.5*porod_exp)*gammainc(0.5*porod_exp, usub) -
                  upow*gamma(porod_exp)*gammainc(porod_exp, usub)))
    return result

#==== correlation_length ====
def Iq2(q, lorentz_scale, porod_scale, cor_length, porod_exp, lorentz_exp):
    p = (q + 2) / 3
    p = q + 2 / 3
    porod = porod_scale / q**porod_exp
    lorentz = lorentz_scale / (1.0 + (q * cor_length)**lorentz_exp)
    inten = porod + lorentz
    return inten

#==== unified_power_Rg ====
# rg, power, B and G are vector parameters, which we know from the model definition file,
# but can only guess at by looking at the code
def Iq41(q, level, rg, power, B, G, c2, c1, a2):
#    result = G[7]
    iStart=2
    iEnd=200
    iStep=5
    for i in range(1,10,2):
        print(i)
    for n in range(iStart,iEnd,iStep):
        print(n)
    p_val = np_polyval([c2, c1, a2], q**2)
    level = int(level + 0.5)
    if level == 0:
        return 1./q

    result = 0.0
#    x = 0
#    y = 1
    x1, x2, x3 = x, y, 17.0
    if q == 0:
        for i in range(level):
            result += G[i]
    else:
        for i in range(1,level,2):
            exp_now = exp(-(q*rg[i])**2/3.)
            pow_now = (erf(q*rg[i]/sqrt(6.))**3/q)**power[i]
            if i < level-1:
                exp_next = exp(-(q*rg[i+1])**2/3.)
            else:
                exp_next = 1
            result += G[i]*exp_now + B[i]*exp_next*pow_now
    return result

#==== poly_gauss_coil ====
# Includes a taylor series with polynomial evaluation. 
# There are a lot of these in the C code, so this could be pretty common,
# and it may be worth supporting it.  Short term, better to not do anything
# fancy and instead have the user write:
#    p2 = ...
#    p1 = ...
#    p0 = ...
#    result = ((p2*z + p1)*z + p0
def Iq12(q, i_zero, rg, polydispersity):
    u = polydispersity - 1.0
    z = q**2 * (rg**2 / (1.0 + 2.0*u))

    # need to trap the case of the polydispersity being 1 (ie, monodisperse!)
    if polydispersity == 1.0:
        if q != 0:
            result = 2.0 * (expm1(-z) + z)
            result /= z**2
        else:
            result = 1.0
    else:
        # Taylor series around z=0 of (2*(1+uz)^(-1/u) + z - 1) / (z^2(u+1))
        p = [
            #(-1 - 20*u - 155*u**2 - 580*u**3 - 1044*u**4 - 720*u**5) / 2520.,
            #(+1 + 14*u + 71*u**2 + 154*u**3 + 120*u**4) / 360.,
            #(-1 - 9*u - 26*u**2 - 24*u**3) / 60.,
            (+1 + 5*u + 6*u**2) / 12.,
            (-1 - 2*u) / 3.,
            (+1),
            ]
        if z > 1e-4:
            result = 2.0 * (power(1.0 + u*z, -1.0/u) + z - 1.0) / (1.0 + u)
            result /= z**2
        else:
            result = np.polyval(p, z)
    return i_zero * result

#==== broad_peak ====
def Iq1(q, porod_scale, porod_exp, lorentz_scale, lorentz_length, peak_pos, lorentz_exp):
    z = abs(q - peak_pos) * lorentz_length
    inten = (porod_scale / q ** porod_exp
                + lorentz_scale / (1 + z ** lorentz_exp))
    return inten

def MultAsgn(a, b):
#    m = [i for i in range(10)]
    p = [1,2,3,4,5]
    z = [1,2]
    result = polyval(p, z)#np.polyval(p, z)

    sqr1 = d ** 2.5
    sqr = d ** 2
    sqr1 = d ** -2
    sqr1 = d ** a

    cub = d ** 3
    rut = d ** (1/2)
    cut = d ** (1/3)
    cut_n = d ** -(1/3)
    rut = d ** 0.5
    ar = [1,2,3]
    ar2 = [4, 5, 6]
    c = a * b
    d = c / b
    e = b // a
    c, d = a + b, a - b
    d = a ** b
    r = d ** (-2)
    c = d ** 2
    c = b ** 3
    r = d ** (-2)
    alpha = 30 * pi / 180.0
    SINCOS (alpha, beta, s, c)

#==== gauss_lorentz_gel ====
def Iq3(q, gauss_scale, cor_length_static, lorentz_scale, cor_length_dynamic):
    term1 = gauss_scale *\
            exp(-1.0*q*q*cor_length_static*cor_length_static/2.0)
    term2 = lorentz_scale /\
            (1.0+(q*cor_length_dynamic)*(q*cor_length_dynamic))

    return term1 + term2

#==== guinier_porod ====
def Iq4(q, rg, s, porod_exp):
    n = 3.0 - s
    ms = 0.5*(porod_exp-s) # =(n-3+porod_exp)/2

    # Take care of the singular points
    if rg <= 0.0 or ms <= 0.0:
        return 0

    # Do the calculation and return the function value
    if q < sqrt(n*ms)/rg:
        iq = q**-s * exp(-(q*rg)**2/n)
    else:
        iq = q**-porod_exp * (exp(-ms) * (n*ms/rg**2)**ms)
    return iq

#==== line ====
def Iq5(q, intercept, slope):
    inten = intercept + slope*q
    return inten

#==== porod ====
def Iq7(q):
    return q**-4

#==== power_law ====
def Iq8(q, power):
    result = q** -power
    return result

#==== spinodal ====
def Iq9(q, gamma, q_0):
    x = q/q_0
    inten = ((1 + gamma / 2) * x ** 2) / (gamma / 2 + x ** (2 + gamma))
    return inten

#==== two_lorentzian ====
def Iq10(q, lorentz_scale_1, lorentz_length_1, lorentz_exp_1, lorentz_scale_2, lorentz_length_2, lorentz_exp_2):
    intensity  = lorentz_scale_1/(1.0 +
                                  power(q*lorentz_length_1, lorentz_exp_1))
    intensity += lorentz_scale_2/(1.0 +
                                  power(q*lorentz_length_2, lorentz_exp_2))
    return intensity


#==== two_power_law ====
def Iq11(q,
      coefficent_1=1.0,
      crossover=0.04,
      power_1=1.0,
      power_2=4.0,
      ):
    coefficent_2 = coefficent_1 * power(crossover, power_2 - power_1)
    if q <= crossover:
        result = coefficent_1 * power(q, -power_1)
    else:
        result = coefficent_2 * power(q, -power_2)
    return result

#==== teubner_strey ====
# another call to np.polyval, but this would be pretty easy to replace with
#    qsq = q**2
#    inten = ((c2*qsq + c1)*qsq + a2
#    return 1.0e-4*prefactor / inten
def Iq13(q, volfraction_a, sld_a, sld_b, d, xi):
    drho = sld_a - sld_b
    k = 2.0*pi*xi/d
    a2 = (1.0 + k**2)**2
    c1 = 2.0*xi**2 * (1.0 - k**2)
    c2 = xi**4
    prefactor = 8.0*pi * volfraction_a*(1.0 - volfraction_a) * drho**2 * c2/xi
    return 1.0e-4*prefactor / np_polyval([c2, c1, a2], q**2)
#    return 1.0e-4*prefactor / np.polyval([c2, c1, a2], q**2)


#==== unified_power_Rg ====
# rg, power, B and G are vector parameters, which we know from the model definition file,
# but can only guess at by looking at the code
def Iq14(q, level, rg, power, B, G):
    level = int(level + 0.5)
    if level == 0:
        return 1./q

    result = 0.
    if q == 0:
#        for i in range(foo(j, k)):
#            q += 2
        for i in range(level):
            result += G[i]
    else:
        for i in range(level):
            exp_now = exp(-(q*rg[i])**2/3.)
            pow_now = (erf(q*rg[i]/sqrt(6.))**3/q)**power[i]
            if i < level-1:
                exp_next = exp(-(q*rg[i+1])**2/3.)
            else:
                exp_next = 1
            result += G[i]*exp_now + B[i]*exp_next*pow_now
    return result

