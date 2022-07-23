import urllib.request as ur
import xml.etree.ElementTree as ET

total = 0

my_url = input('Enter the location : ')

xml = ur.urlopen(my_url).read()

print(f'Total Charachters : {len(xml)}')

tree = ET.fromstring(xml)

lst = tree.findall('.//comment')

for item in lst :
    print('Name : ', item.find('name').text)
    print('Count : ', item.find('count').text)
    print('---'* 10)
    try :
        number = item.find('count').text
        number = int(number)
    except Exception as e:
        print('Problem : {}'.format(e))
    
    total += number

print('Total = ', total)