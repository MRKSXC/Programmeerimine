#!/usr/bin/python
# coding: latin-1

Visiitkaart = raw_input('Sisesta visiitkaardi nimi :')
Ettev6te = raw_input('Sisesta ettevõtte nimi :')
Nimi = raw_input('Sisesta oma nimi :')
Amet = raw_input('Sisesta oma amet :')
Kontakt = raw_input('Sisesta Telefoni number :')

Tyhjus = ' '
Joon = '-'

print '<', Joon.center(60,'-'), '>'
print '/', Tyhjus.center(60,' '), '\ '
print '|', Visiitkaart.center(60,' '),  '|'
print '|', Ettev6te.center(60,' '),	'|'
print '|', Tyhjus.center(60,' '),	  '|'
print '|', Nimi.center(60,' '),		  '|'
print '|', Amet.center(60,' '),		  '|'
print '/', Kontakt.center(60,' '),  '\ '
print '>', Joon.center(60,'-'),		  '<'


