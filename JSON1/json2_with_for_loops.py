import json

data = """[
    {   "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x"  : "7",
        "name" : "Dogukan" 
    }
]"""

info = json.loads(data)
count = 0
for item in info :
    print(f'Person{count+1} ID : ', item["id"])
    print(f'Person{count+1} X : ', item["x"])
    print('Person{0} Name : '.format(count+1), item["name"])
    count += 1
    print('---'*5)