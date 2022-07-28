import json 

with open('/Users/dogukan/Desktop/INTRO_PYT_DJANGO/my_Project1/data.json', 'r') as read_file :
    with open('/Users/dogukan/Desktop/INTRO_PYT_DJANGO/JSON1/new_json_file1.json', 'w') as write_file:
        for item in read_file.read() :
            write_file.write(item)
        

with open('/Users/dogukan/Desktop/INTRO_PYT_DJANGO/JSON1/new_json_file1.json', 'r') as read_file :
    print(read_file.read())