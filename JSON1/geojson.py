import urllib.request, urllib.parse, urllib.error
import json
import ssl




serviceurl = 'https://maps.googleapis.com/maps/api/directions/json?'
while True :
    adress = input('Enter the location : ')
    if len(adress) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'adress' : adress})

    print(url, 'is retrieving......')
    uh = urllib.request.urlopen(url).read()         #Sertifika hatasi veriyor ????
    data = uh.decode()
    
    print(len(data), 'characters retrieved!')

    try : 
        js = json.load(uh)

    except :
        js = None

    if not js or 'status' not in js or js['status'] != 'OK' :
        print('====== Failure To Retrieve =======')
        print(data)
        continue
    
    print(json.dumps(js, indent=4))         #bÜTÜN JSON KOD DÖKÜMÜNÜ EKRANA YAZDIRIR.

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    name = js['results'][0]['adress_components'][2]['short_name']
    location = js['results'][0]['formatted_adress']

    print('lat : {0}'.format(lat))
    print('lng : {0}'.format(lng))
    print('Name : {}'.format(name))
    print(location)


    