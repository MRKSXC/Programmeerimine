#!/usr/bin/python
# coding: latin-1
import os
clear = os.system('clear');

print '{:-^75}'.format('Arve')
print
Arve = '{:<30} {:<20} {:<20} {:>10}'
Saatmine = '{:<31} {:<21} {:<21} {:>10}'
Aadress = '{:<29} {:<10}'
kaubad = '{:<19}{:>15}{:>15}{:>15}'
Raha = '{:>49}{:>15}'
K2ibemaks = '{:>50}{:>15}'
Kontaktid = '{:-<30}{:-<60}'

print Arve.format('Arve väljastaja', 'Arve saaja','Arve number:','A-561482')
print Saatmine.format('Ziguli Õlu','Säästu Kange','Kuupäev:','10.02.2013')
print Aadress.format('Vildetee 26','Saarepuu 9-54')
for x in xrange(1,5):
    print
    pass
print kaubad.format('Kaup','Hind','Kogus/KG','Kokku')
print kaubad.format('Algis','200.0','7.0','1400.0')
print kaubad.format('Pelmeenid','16.0','3.0','48.0')
print kaubad.format('Saepuru','175','6.0','1050.0')
print kaubad.format('Tikutops','05.0','15.0','7.5.0')
print
print Raha.format('Vahesumma', '2505,5')
print K2ibemaks.format('Käibemaks 20%', '501,1')
print Raha.format('Kokku', '3006,6')
for x in xrange(1,2):
    print
    pass
print Kontaktid.format('Kontaktid','Arveldus')
print Kontaktid.format('Keegi.miski@kuskil.com','Mingi Puu AS')
print Kontaktid.format('Tel: 15178421','FIFA 13123213623125122')
