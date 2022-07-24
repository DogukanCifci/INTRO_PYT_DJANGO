
import urllib.request as ur 
import json 

my_url = input("Enter the location : ")
print(my_url, 'is retrieving......')

data = ur.urlopen(my_url).read().decode('utf-8')
print(f'{len(data)} characters received!!')

counter = 0
total = 0
js = json.loads(data)

for item in js['comments'] :
    name = item['name']
    #print(f'Name : {name}')
    
    count = item['count']
    #print(count)

   # print('--'*10)
    counter += 1
    try : 
        count = int(count)

    except Exception as e :
        print(f'=======ERROR====== {e}')

    total += count 
print(f'Total : {counter}')
print('Sum= {0}'.format(total))