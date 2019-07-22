import os, sys, getopt
#------------------------------------------------------------------------------
def get_param_res_dir (params):
    res_dir = None
    try:
        options, remainder = getopt.getopt(params, '', ['store='])
    except Exception as e:
        print(f'get_param_res_dir runtime error: {e}') 
        exit(1) 
    for opt, arg in options:
        if opt in ('--store'):
            res_dir = arg.strip();
    try:
        res_file = os.path.splitext(os.path.basename(remainder[0]))[0]
    except:
        res_file = 'results'
    return res_dir, res_file
#------------------------------------------------------------------------------
def get_results_directory (params):
    res_dir, res_file = get_param_res_dir(params)
    if res_dir == None:
        n = 1
        base_res = os.getcwd() + os.sep
        if res_file:
            base_res += res_file
        else:
            base_res += 'resuts'
        candidate = base_res
        params.append('--store')
        params.append(candidate)
    else:
        candidate = res_dir
    return candidate
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
