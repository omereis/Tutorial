from res_dir import get_results_directory
#------------------------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) < 2:
        params = ['/usr/local/lib/python2.7/dist-packages/bumps/cli.py','/home/bumps/celery/problems/cf1.py', '--batch', '--stepmon', '--burn=100', '--steps=100', '--store=/home/bumps/celery/problems/results', '--fit=newton']
        params = params[1:]
    else:
        params = sys.argv[1:]
    results_dir = get_results_directory(params)
    print(f'\nResults dir: "{results_dir}"')
