largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
    
    try :
        num = int(num)
        
        
    except :
        print('Invalid input')
        continue
    
    
    if num > largest :
        largest = num
        continue
    
    if num < smallest :
        smallest = num
        continue
        
    

print("Maximum", largest)
print('Minimum', smallest)