import json 

data = """{"Musteri" : [{ 
    "name" : "Dogukan",
    "surname" : "Cifci",
    "tel" : {
        "hide" : "yes"
    }
    
},
{
    "name" : "Mirac",
    "surname" : "iscan",
    "tel" : {
        "hide" : "yes"
    }
}
]
}"""


file = json.loads(data)
with open("/Users/dogukan/Desktop/INTRO_PYT_DJANGO/JSON1/dump.json", "w") as write_file :
    new_file = json.dump(file, write_file)

with open("/Users/dogukan/Desktop/INTRO_PYT_DJANGO/JSON1/dump.json", "r") as read_file :
    print(read_file.read())