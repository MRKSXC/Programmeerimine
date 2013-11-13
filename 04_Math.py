#!/usr/bin/python
# coding: latin-1
import math
import os
clear = os.system('clear')

print 'Kui kolmnurga üks kaatet on 12m,'
print 'Leia hüpotenuus sin ja cos abil ja lähiskaatet tan abil'
print 'Alfa = 30*, b = 12m'
print

vastustan = 12*math.tan(30*math.pi/100)
vastussin = 12*math.sin(30*math.pi/100)
vastuscos = 16.52*math.cos(30*math.pi/100)
print 'Lähiskaatet = ', round(vastustan,2)
print 'Sin30* =', round(vastussin,2)
print 'Cos30* =', round(vastuscos,2)
print 'Tan30* =', round(vastustan,2)
print
print 'Hüpotenuus = ', round(vastussin,2)
print
print

