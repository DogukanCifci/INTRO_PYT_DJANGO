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
        
    if largest == None :            #!!!!1 Öncelikle bunlari esitlemeliyiz yoksa altta > largest veya smallest yapamayi cünkü > < ve None type birbirini desteklemiyor!!!!!1
        largest = num
    
    
    if smallest == None :
        smallest = num  
    
    
    if num < smallest :
        smallest = num
        
        
    if num > largest :
        largest = num
        
        
       
print("Maximum is", largest)
print('Minimum is', smallest)