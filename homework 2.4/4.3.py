from sys import stdin
from  functools import  reduce


print(reduce(lambda a, b: a if (a < b) else b, [line for line in stdin]))