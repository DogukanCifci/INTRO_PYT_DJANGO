#in 10^6 
entfernungen  = {
    'Merkur' : 58, 
    'Venus' : 108,
    'Erde' : 150,
    'Mars' : 228,
    'Jupiter' :778,
    'Saturn' :1427,
    'Uranus' :2884,
    'Neptun' :4509
}


umrechnungen = {
    'km' : 1,
    'm' : 1000,
    'dm' : 10000,
    'cm' : 100000
}

angefragte_planet = input('Bitte geben Sie den Namen des Planeten : ').title()
angefragte_einheit = input('In welcher Einheit soll die Entefernung angezeigt werden? : ').lower()

ergebnis = entfernungen[angefragte_planet] * 1000000 * umrechnungen[angefragte_einheit]

print(f'Der Planet {angefragte_planet} hat eine Entfernung von {ergebnis} {angefragte_einheit} zur Sonne.')

print('or')

print('Der Planet {} ist {} {} entfernt'.format(angefragte_planet, ergebnis, angefragte_einheit))