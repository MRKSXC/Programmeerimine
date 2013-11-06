#!/usr/bin/python
# coding: latin-1

Pealk1 = raw_input('Pealkiri 1 :')
Pealk2 = raw_input('Pealkiri 2 :')
Header = raw_input('Sisesta Header :')
Footer = raw_input('Sisesta Footer :')
Tekst1 = raw_input('Sisesta esimene tekst :')
Tekst2 = raw_input('Sisesta Teine tekst :') 
Tyhi = ' '
Joon = '-'

print Header.center(60, '-')
print Tyhi.center(60, ' ')
print Pealk1.center(60, ' ')
print Tyhi.center(40, ' ')
print Tekst1.center(50, ' ')
print Joon.center(60, '-')        

print Tyhi.center(60, ' ')
print Pealk2.center(60, ' ')
print Tyhi.center(60, ' ')
print Tekst2.center(40, ' ')
print Tyhi.center(60, ' ')
print Footer.center(60, '-')
print Joon.center(60, '-')
