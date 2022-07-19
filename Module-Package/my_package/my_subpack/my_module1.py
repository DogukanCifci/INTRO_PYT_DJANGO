""" Bu benim ilk modülüm... Test amaçlı yazıldı"""
def my_func1(x):
    return x**2
def my_func2(y):
    print(*y)




if __name__=="__main__":
    # doğrudan script gibi çalıştıracaksan (yani ana/main program isem) beni çalıştır
    # yoksa (import edileceksem) aşağıdaki kodları çalıştırma
    print("hello")
    print(my_func1(3))
    my_func2("clarusway")