#escriba un algoritmo para poner gasolina desde un dispensador de gasolina
import time

def dispensador():
    print("bienvenido a el dispensador automatico de gasolina")
    time.sleep(1)
    print("por favor abrir la tapa del vehiculo")
    time.sleep(1)
    tapa = input("abrir la tapa si o no: ")
    time.sleep(1)
    if tapa == "si":
        print("tapa de vehiculo abierta")
        return llenar()
    else:
        print("lo siento si la tapa esta cerrada no podemos ayudarlo HASTA LUEGO!")

def llenar():
    print("que gasolina desea Gasolina 95 o 91")

    gasolina = int(input())
    if gasolina == 91:
        tanque = input("desea medio tanque o tanque full: ")
        if tanque == "tanque full":
            print("espere unos minutos por favor usted eligio tanque full")
            time.sleep(3)
            print("tanque full muchas gracias por venir")
        
        else:
            print("espere unos minutos por favor usted eligio medio tanque")
            print("medio tanque listo muchas gracias por venir")
          
    else:
        print("lo sentimos no tenemos 95 vuelva despues")

    


dispensador()