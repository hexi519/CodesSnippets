import os
import sys
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

from .subTree.m3 import printSelf,m4
printSelf()
m4.printSelf()