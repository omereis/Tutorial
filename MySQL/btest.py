import sys

def main(argv):
    for i in range(len(argv)):
#        print("%d: %s" % (i, str(argv[i])))
        print("{}: {}".format(i,argv[i]))

if __name__ == '__main__':
    main(sys.argv)

