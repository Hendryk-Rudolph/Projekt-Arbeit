import random

Dateiname = 'namen.txt'
vornamenliste = []
nachnamenliste = []
Number_ID = 1000

def write_ln(_ID, vorname, nachname):
    my_file = open(Dateiname, 'a')
    my_string = str(_ID) + ', ' + nachname + ', ' + vorname + '\n'
    my_file.write(my_string)
    my_file.close()
    
my_file = open('vornamen.txt', 'r')
zeilen = my_file.readlines()
for zeile in zeilen:
    vornamenliste += [zeile[:-1]]
my_file.close()

my_file = open('nachnamen.txt', 'r')
zeilen = my_file.readlines()
for zeile in zeilen:
    nachnamenliste += [zeile[:-1]]
my_file.close()

my_file = open(Dateiname, 'w')
my_file.close()
for _ID in range(Number_ID):
    vorname = random.choice(vornamenliste)
    nachname = random.choice(nachnamenliste)
    write_ln(_ID, vorname, nachname)