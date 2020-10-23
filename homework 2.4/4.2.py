from functools import reduce
import sys
from math import gcd


print(reduce(lambda x, y: gcd(x, y), [int(line) for line in sys.stdin]))