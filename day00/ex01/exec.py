import sys

print(" ".join(sys.argv[1:len(sys.argv):1]).swapcase()[::-1], end=' ')
