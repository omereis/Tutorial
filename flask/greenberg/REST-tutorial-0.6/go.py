import getopt
import sys

version = '1.0'
verbose = False
output_filename = 'default.out'

port=5000
host='0.0.0.0'

print('ARGV      :', sys.argv[1:])

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        'p:h:',
        ['port=',
         'host=',
         ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

print('OPTIONS   :', options)

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg
    elif opt == '-p':
        port = arg
    elif opt == '-h':
        host = arg

print('VERSION   :', version)
print('VERBOSE   :', verbose)
print('OUTPUT    :', output_filename)
print('REMAINING :', remainder)
print('============',)
print('Port      :', port)
print('Host      :', host)


