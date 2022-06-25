hrs = input("Enter Hours:")

try : 
    hours = int(hrs)
    
    rate = 10.5

except : 
    print("You didnt enter a number")


if hours < 40 :
    payment = hours * 10.5
    
else :
    a = hours - 40
    payment = 40 * 10.5 + a * 10.5 * 1.5
  #  payment = (40 * 10.5) + (hours - 40) * 10.5 * 1.5  -----> Optional
print(payment)



score = input("Enter Score: ")

try :
    score_1 = float(score)
    
except : 
    print('You didnt a numerical input. Please try again!')
    
if score_1 > 1 :
    print('You entered invalid number')
    
elif score_1 >= 0.9 :
    print('A')
    
elif score_1 >= 0.8 :
    print('B')
    
elif score_1 >= 0.7 :
    print('C')
    
elif score_1 >= 0.6 :
    print('D')
    
elif score_1 <0.6 :
    print('F')