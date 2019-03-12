#include <math.h>

#line 1 "iq_num.py"
double Iq4(double q, double rg, double s, double porod_exp)

{

    double n, ms, iq;



    n = (3.0 - s);

    ms = (0.5 * (porod_exp - s));

    if ((rg <= 0.0) || (ms <= 0.0)) {

        return(0);

    }

    if (q < (sqrt((n * ms)) / rg)) {

        iq = ((pow(q, (-s)) ) * exp(((-(square((q * rg)) )) / n)));

    }

    else {

        iq = ((pow(q, (-s)) ) * exp(((-(square((q * rg)) )) / n)));

    }

    return(iq);

}


double Iq2(double q, double lorentz_scale, double porod_scale, double cor_length, double porod_exp, double lorentz_exp)

{

    double p, porod, lorentz, inten;



    p = ((q + 2) / 3);

    p = (q + (2 / 3));

    porod = (porod_scale / (pow(q, porod_exp) ));

    lorentz = (lorentz_scale / (1.0 + (pow((q * cor_length), lorentz_exp) )));

    inten = (porod + lorentz);

    return(inten);

}


double Iq41(double q, double level[], double rg, double power, double B, double G[], double c2, double c1, double a2)

{

    int i;

    double iStart, iEnd, iStep, p_val, result, x, y, x1, x2, x3;

    double vec1[] = {c2, c1, a2};



    iStart = 2;

    iEnd = 200;

    iStep = 5;

    p_val = polyval(vec1, (square(q) ), 3);

    level[0] = (int) ((level[0] + 0.5));

    if (level[0] == 0) {

        return((1.0 / q));

    }

    result = 0.0;

    x = 0;

    y = 1;

    x1 = x;

    x2 = y;

    x3 = 17.0;

    if (q == 0) {

        for(i=0 ; i < level[0] ; i += 1) {

            result += G[i];

        }

    }

    else {

        for(i=0 ; i < level[0] ; i += 1) {

            result += G[i];

        }

    }

    return(result);

}


double Iq12(double q, double i_zero, double rg, double polydispersity)

{

    double u, z, result;



    u = (polydispersity - 1.0);

    z = ((square(q) ) * ((square(rg) ) / (1.0 + (2.0 * u))));

    if (polydispersity == 1.0) {

        if (q != 0) {

            result = (2.0 * (expm1((-z)) + z));

            result /= (square(z) );

        }

        else {

            result = (2.0 * (expm1((-z)) + z));

            result /= (square(z) );

        }

    }

    else {

        if (q != 0) {

            result = (2.0 * (expm1((-z)) + z));

            result /= (square(z) );

        }

        else {

            result = (2.0 * (expm1((-z)) + z));

            result /= (square(z) );

        }

    }

    return((i_zero * result));

}


double Iq1(double q, double porod_scale, double porod_exp, double lorentz_scale, double lorentz_length, double peak_pos, double lorentz_exp)

{

    double z, inten;



    z = (fabs ((q - peak_pos)) * lorentz_length);

    inten = ((porod_scale / (pow(q, porod_exp) )) + (lorentz_scale / (1 + (pow(z, lorentz_exp) ))));

    return(inten);

}


double MultAsgn(double a, double b)

{

    double *p, *ar, *ar2;

    double sqr1, d, sqr, cub, rut, cut, cut_n, c, e, r, alpha, pi, s;

    double vec1[] = {1, 2, 3, 4, 5};

    double vec2[] = {1, 2, 3};

    double vec3[] = {4, 5, 6};



    p = vec1;

    sqr1 = (pow(d, 2.5) );

    sqr = (square(d) );

    sqr1 = (1.0 /(square(d)) );

    sqr1 = (pow(d, a) );

    cub = (cube(d) );

    rut = (sqrt(d) );

    cut = (cbrt(d) );

    cut_n = (1.0 /(cbrt(d)) );

    rut = (sqrt(d) );

    ar = vec2;

    ar2 = vec3;

    c = (a * b);

    d = (c / b);

    e = ((int)(b) /(int)(a));

    c = (a + b);

    d = (a - b);

    d = (pow(a, b) );

    r = (1.0 /(square(d)) );

    c = (square(d) );

    c = (cube(b) );

    r = (1.0 /(square(d)) );

    alpha = ((30 * pi) / 180.0);

    s = sin(alpha);

    c = cos(alpha);

    return(((square(s) ) + (square(c) )));

}


double Iq3(double q, double gauss_scale, double cor_length_static, double lorentz_scale, double cor_length_dynamic)

{

    double term1, term2;



    term1 = (gauss_scale * exp(((((((-1.0) * q) * q) * cor_length_static) * cor_length_static) / 2.0)));

    term2 = (lorentz_scale / (1.0 + ((q * cor_length_dynamic) * (q * cor_length_dynamic))));

    return((term1 + term2));

}


double Iq5(double q, double intercept, double slope)

{

    double inten;



    inten = (intercept + (slope * q));

    return(inten);

}


double Iq6(double q, double rg, double porod_exp)

{

    double usub, result;



    usub = ((((square((q * rg)) ) * ((2.0 / porod_exp) + 1.0)) * ((2.0 / porod_exp) + 2.0)) / 6.0);

    if (q <= 0) {

        result = 1.0;

    }

    else {

        result = 1.0;

    }

    return(result);

}


double Iq7(double q)

{

    return((1.0 /(pow(q, (-4))) ));

}


double Iq8(double q, double power)

{

    double result;



    result = (pow(q, (-power)) );

    return(result);

}


double Iq9(double q, double gamma, double q_0)

{

    double x, inten;



    x = (q / q_0);

    inten = (((1 + (gamma / 2)) * (square(x) )) / ((gamma / 2) + (pow(x, (2 + gamma)) )));

    return(inten);

}


double Iq10(double q, double lorentz_scale_1, double lorentz_length_1, double lorentz_exp_1, double lorentz_scale_2, double lorentz_length_2, double lorentz_exp_2)

{

    double intensity;



    intensity = (lorentz_scale_1 / (1.0 + pow((q * lorentz_length_1), lorentz_exp_1)));

    intensity += (lorentz_scale_2 / (1.0 + pow((q * lorentz_length_2), lorentz_exp_2)));

    return(intensity);

}


double Iq11(double q, double coefficent_1, double crossover, double power_1, double power_2)

{

    double coefficent_2, result;



    coefficent_2 = (coefficent_1 * pow(crossover, (power_2 - power_1)));

    if (q <= crossover) {

        result = (coefficent_1 * pow(q, (-power_1)));

    }

    else {

        result = (coefficent_1 * pow(q, (-power_1)));

    }

    return(result);

}


double Iq13(double q, double volfraction_a, double sld_a, double sld_b, double d, double xi)

{

    double drho, k, pi, a2, c1, c2, prefactor;

    double vec1[] = {c2, c1, a2};



    drho = (sld_a - sld_b);

    k = (((2.0 * pi) * xi) / d);

    a2 = (square((1.0 + (square(k) ))) );

    c1 = ((2.0 * (square(xi) )) * (1.0 - (square(k) )));

    c2 = (pow(xi, 4) );

    prefactor = ((((((8.0 * pi) * volfraction_a) * (1.0 - volfraction_a)) * (square(drho) )) * c2) / xi);

    return(((0.0001 * prefactor) / polyval(vec1, (square(q) ), 3)));

}


double Iq14(double q, double level[], double rg, double power, double B, double G[])

{

    int i;

    double result;



    level[0] = (int) ((level[0] + 0.5));

    if (level[0] == 0) {

        return((1.0 / q));

    }

    result = 0.0;

    if (q == 0) {

        for(i=0 ; i < level[0] ; i += 1) {

            result += G[i];

        }

    }

    else {

        for(i=0 ; i < level[0] ; i += 1) {

            result += G[i];

        }

    }

    return(result);

}


double check()

{

    double y, k, total;



    y = 3 if  else 0 if  else 1;

    k = 1;

    total = 0.0;

    while (k < 3):

        total += (cube(k) );

        k += 1;

    print(('check total %g' % total));

    return(total);

}


if (__name__ == '__main__') {

    check()

}
