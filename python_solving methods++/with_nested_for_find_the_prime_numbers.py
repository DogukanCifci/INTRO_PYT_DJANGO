while True :
  number = input("Enter a number : ")
  if number.isdigit() :
    number = int(number)
    break
  else :
    print('Invalid Input.Please try again ')
    continue 

my_list = list()
for i in range(2, number+1) :
  status = True
  for ii in range(2, i) :
    if i % ii == 0 :
      status = False
    
  if status == True :
    my_list.append(i)


print(my_list)
