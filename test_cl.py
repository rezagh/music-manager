import sys
from getopt import getopt

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

opts, args = getopt(sys.argv[1:],"c:d:")
for opt, arg in opts:
    if opt == '-c':
        print '-c is ' + arg
    elif opt == '-d':
        print '-d is ' + arg
    elif opt == 's':
        print 's is ' + arg

print 'end'