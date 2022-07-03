from isort import file

#1. Method
with open("/Users/dogukan/Desktop/INTRO_PYT_DJANGO/python_solving methods++/mbox-short.txt", "r") as File1 :
    file_stuff = File1.readlines()

    #print(file_stuff)

    print(file_stuff[0]) #-------> Ilk satir anlamina gelir. Ciktiya bakarsak sadece ilk satiri almistir
    print(file_stuff[1]) #-------> 2. satir anlamina gelir.

    print(file_stuff[:3]) #------->listelemis bir sekilde bize ilk 3 satiri vericek. Ciktiya bak kesin 


    #Eger bu sekilde yazarsak ;
    file_stuff1 = File1.readlines(16) #--------> Ilk 16 karakteri alir.

    print(file_stuff1)

    file_stuff1 = File1.readlines(5)

    print(file_stuff1)  # --------> Ilk 16 karakterden sonra gelen 5 karakteri alir. En basa dönmez



