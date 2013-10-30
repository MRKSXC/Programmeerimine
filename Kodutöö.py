name = raw_input('Mis on sinu nimi :')
Synniaasta = raw_input('Mis on sinu synniaasta :')

capitalize_name = name.capitalize()
ST = name.isalpha()


if name != capitalize_name:
	print'Suur algust2ht'

	
elif name == capitalize_name:
	print 'sinu nimi on ' + capitalize_name
	print 'sinu synniaasta on ' + Synniaasta
	print 'Name in Uppercase ' + name.upper()
	print 'nimi v2ikestes t2htedes ' + name.lower()
	
if ST == True:
	print 'Jah';
else:
	print 'Ei';

 	



