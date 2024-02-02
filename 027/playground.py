def add(*args):
    soma = 0
    for n in args:
        soma += n
    return soma

# def calculator(**kwargs):
#     for (key, value) in kwargs.items():
#         print(key)
#         print(value)

def calculator(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
 
# class Car:
#     def __init__(self, **kw):
#         self.cor = kw["cor"]
#         self.modelo = kw["modelo"]
class Car:
    def __init__(self, **kw):
        self.cor = kw.get("cor")
        self.modelo = kw.get("modelo")       
    
#main()
#print(f"{add(1, 2, 3, 4)}")

#calculator(2,add=5, multiply=10)

my_car = Car(cor="Branco", modelo="4 Portas")
your_car = Car(modelo = "2 Portas")

print(my_car.cor)
print(my_car.modelo)
print(your_car.modelo)
print(your_car.cor)