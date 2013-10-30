
name = raw_input('Mis on sinu nimi :')
Synniaasta = raw_input('Mis on sinu synniaasta :')

capitalize_name = name.capitalize()
upper_n = name.upper()
ST = name.isalpha();


if name != capitalize_name:
	print'Suur algust2ht'

	
elif name == capitalize_name:
	print 'sinu nimi on ' + capitalize_name
	print 'sinu synniaasta on ' + Synniaasta
	print 'Name in Uppercase ' + name.upper()
	
if name == ST:
	print 'Jah';
else:
	print 'Ei';

 	



