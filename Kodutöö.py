#!/usr/bin/python
# coding: latin-1


name = raw_input('Mis on sinu nimi :')
Synniaasta = raw_input('Mis on sinu sünniaasta :')

capitalize_name = name.capitalize()
ST = name.isalpha();
UP = name.isalpha();



if name != capitalize_name:
	print'Suur algustäht'


	
elif name == capitalize_name:
	print 'sinu nimi on: ' + capitalize_name
	print 'sinu sünniaasta on: ' + Synniaasta

if UP != True:
	print 'Nimes on numbrid, Suurte tähtedega nime ei kuvata'
else:
	print 'Nimi suurte tähtedega: ' + name.upper()

if UP != True:
	print 'Nimes on numbrid, Väikeste tähtedega nime ei kuvata'
else:
	print 'Nimi väikestes tähtedega: ' + name.lower()
	
if ST == True:
	print 'Kas sinu nimes on kõik tähed: Jah';
else:
	print 'Kas sinu nimes on kõik tähed: EI';

 	



