import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "int1",
        "number" : "+1 734 303 4456"
    }, 
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)

print('Name : ', info['name'])
print('Hide : ', info['email']['hide']) #Email kisminin icindeki hide in karsiligini ver.
print('Phone Number : ', info['phone']['number'])   #Ic ice liste olarak düsünüyoruz. phone icindeki number kismini ver
print('Phone Type : ', info['phone']['type'])   #phone icindeki type in karsiligini ver-.

#print('Phone Number : ', info['phone']['number']['type'])   #Yazarsak hata verir . Cünkü type number kisminin icinde degil. Phone kisminin icinde