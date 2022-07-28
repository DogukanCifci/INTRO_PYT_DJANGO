
import json

data = """[
    {
        "id" : "001", "personal_info" : {
            "first_name" : "Dogukan",
            "last_name" : "Cifci",
            "phone_number" : "+1 234 342 12",
            "adress" : {
                "state" : "US",
                "city" : "Washington",
                "post_code" : "98811"
            } ,
            "languages" : ["Python", "JavaScript", "SQL"],
            "experience" : "Junior",
            "mail" : "cifci@gmail.com",
            "sex" : "Male"
        }
        
    },
    {
        "id" : "002" , "personal_info" : {
            "first_name" : "Mirac",
            "last_name" : "Iscan",
            "phone_number" : "+49 234 342 12",
            "adress" : {
                "state" : "Germany",
                "city" : "Stuttgart",
                "post_code" : "73612"
            },
            "languages" : ["Python", "SQL"],
            "experience" : "Mid",
            "mail" : "isgan@gmail.com",
            "sex" : "Male"
        }
    },
    {
        "id" : "003", "personal_info" : {
            "first_name" : "Gizem",
            "last_name" : "Ucar",
            "phone_number" : "+49 224 542 12",
            "adress" : {
                "state" : "Germany",
                "city" : "Aalen",
                "post_code" : "32100"
            }, 
            "languages" : ["Python"],
            "experience" : "Mid",
            "mail" : "None",
            "sex" : "Female"
        }
    }
]"""

file = json.loads(data)


for item in file :
    employee_id = item["id"]
    name = item["personal_info"]["first_name"]
    last_name = item["personal_info"]["last_name"]
    phone_number = item['personal_info']['phone_number']
    state = item["personal_info"]["adress"]["state"]
    languages = item["personal_info"]["languages"]
    experience = item['personal_info']['experience']
    mail = item["personal_info"]['mail']
    print(f"""Employee ID : {employee_id} \n    Name : {name} \n    Surname : {last_name} \n    Phone : {phone_number}
    State : {state}
    Languages : {'-'.join(languages)}
    Experience : {experience}
    Mail-Adress : {mail}""")
    print('-'*10)
    

    
    