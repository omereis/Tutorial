from __future__ import absolute_import, unicode_literals
from .celery import app
#from bumps import cli
import bumps.cli
from .res_dir import get_results_directory
import sys
#------------------------------------------------------------------------------
@app.task
def add(x, y):
    return x + y
#------------------------------------------------------------------------------
@app.task
def mul(x, y):
    return x * y
#------------------------------------------------------------------------------
@app.task
def xsum(numbers):
    return sum(numbers)
#------------------------------------------------------------------------------
def get_param_res_dir (params):
    res_dir = '.'
    try:
        options, remainder = getopt.getopt(params, '', ['store='])
    except Exception as e:
        print(f'get_param_res_dir runtime error: {e}') 
        exit(1) 
    for opt, arg in options:
        if opt in ('-h', '--host'):
            host = arg.strip();
#------------------------------------------------------------------------------
from .oe_debug import print_debug
#------------------------------------------------------------------------------
@app.task
def run_bumps(params):
    try:
        std_out = sys.stdout
        res_dir = get_results_directory (params[1:])
        sa = sys.argv
        sys.argv = params
        #print(f'before: {res_dir}')
        bumps.cli.main()
        #print_debug(f'after: {res_dir}')
        sys.argv = sa
    except Exception as e:
        res_dir = f'{e}'
    #return(cli.main(params))
    finally:
        #print_debug(f'finally: {res_dir}')
        sys.stdout = std_out
    #print(f'after: {res_dir}')
    #print_debug(f'returning: {res_dir}')
    return res_dir
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
