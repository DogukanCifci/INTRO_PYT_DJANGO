
from dataclasses import KW_ONLY


while True :
    mail = input("Mail adresinizi giriniz")

    control = ('@' and '.' in mail) and mail.endswith('com')
    yer = mail.find('@')
    yer2 = mail.find('.', yer)

    if control == False or yer2 < yer:
        print('Invalid Email')
        continue
    
    elif yer2 > yer and control == True :
        break
 
print('Valid Email')
   


