
from __future__ import division
import sys
import os

q1 = input('enter q1: ')
q2 = input('enter q2: ')
p1 = input('enter p1: ')
p2 = input('enter p2: ')

quantMidPoint = (q2 - q1) / (q2+q1/(2))
priceMidPoint = (p2 - p1) / (p2+p1/(2))
elasticity = float(quantMidPoint / priceMidPoint)

if elasticity == 1:
    print ' unit elastic'
elif elasticity <=1:
    answer = format(elasticity, '.5f')
    print ' inelastic: ', answer
else:
    answer = format(elasticity, '.5f')
    print ' elastic: ', answer
