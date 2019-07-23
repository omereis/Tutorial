from __future__ import absolute_import, unicode_literals
from .celery import app
import bumps.cli
from .res_dir import get_results_directory
import sys
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
