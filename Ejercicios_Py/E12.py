# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad 
#(puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
#Crea sus métodos get, set y toString. Tendrá dos métodos especiales:
    # - ingresar(double cantidad): se ingresa una cantidad a la cuenta si la cantidad introducida es negativa, no se hará nada.
    #- retirar(double cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan es negativa, 
    #la cantidad de la cuenta pasa a ser 0.

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    #metodos get
    def get_titular(self):
        return self.titular
    
    def get_cantidad(self):
        return self.cantidad

    #metodos set
    def set_titular(self, titular):
        self.titular = titular
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    
    #metodo tuString
    def __str__(self):
        return (f"Titular: {self.titular}, Cantidad: {self.cantidad}'")
    
    #metodo ingresar dinero
    def ingresar(self, ingreso):
        if ingreso >= 0 :
            self.cantidad += ingreso
        else :
            print ("la cuenta está en negativo")
    
    #metodo retirar dinero
    def retirar (self, retirada):
        if self.cantidad - retirada < 0:
            self.cantidad = 0
        else:
            self.cantidad -= retirada


cuenta = Cuenta('Juan', 5000)
print(cuenta)
cuenta.ingresar(200)
print(cuenta)
cuenta.retirar(8000)
print(cuenta)

