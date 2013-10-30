name = raw_input('Mis on sinu nimi :')
Synniaasta = raw_input('Mis on sinu synniaasta :')

capitalize_name = name.capitalize()
ST = name.isalpha()


if name != capitalize_name:
	print'Suur algust2ht'

	
elif name == capitalize_name:
	print 'sinu nimi on ' + capitalize_name
	print 'sinu synniaasta on ' + Synniaasta
	print 'Nimi suurtet2htedega ' + name.upper()
	print 'Nimi v2ikestes t2htedega ' + name.lower()
	
if ST == True:
	print 'Kas sinu nimes on k6ik t2hed: Jah';
else:
	print 'Kas sinu nimes on k6ik t2hed: EI';

 	



