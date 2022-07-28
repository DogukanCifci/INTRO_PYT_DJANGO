import json 

with open('/Users/dogukan/Desktop/INTRO_PYT_DJANGO/my_Project1/data.json', 'r') as json_file : 
    data = json.load(json_file)
    for item in data :
        try :
            employee_id = item["id"]
            name = item["personal_info"]["first_name"]
            last_name = item["personal_info"]["last_name"]
            phone_number = item['personal_info']['phone_number']
            state = item["personal_info"]["adress"]["state"]
            languages = item["personal_info"]["languages"]
            experience = item['personal_info']['experience']
            mail = item["personal_info"]['mail']
            mail2 = item['personal_info']['mail1']
        except Exception as e :
            print()
            print('Something gone wrong here -- Error :  {0}'.format(e))
            print()
        
        
        
        print(f"""Employee ID : {employee_id}
        Name : {name}
        Surname : {last_name}
        Phone : {phone_number}
        State : {state}
        Languages : {'-'.join(languages)}
        Experience : {experience}
        Mail-Adress : {mail}""")
        print('-'*10)

    print('Thank You for Your Visiting!')
        
    



    
    