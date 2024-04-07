saldo=50
while True:
    print("1.CONSULTAR SALDO")
    print("2.RETIRO")
    print("3.DEPOSITO")
    print("4.SALIR")
    opciones=int(input("seleccione una opcion"))
    if opciones==1:
        print(f"Saldo actual es:${saldo}")
    elif opciones==2:
           retiro=int(input("INGRESE LA CANTIDAD A RETIRAR :$"))
           if retiro>saldo:
            print("RETIRO NO PROCEDE  ")
           else:
               saldo<=retiro
               print("RETIRO EFECTUADO",retiro)
    elif opciones==3:
        
            deposito=int(input("ingrese la cantidad a depositar"))
            saldo+=deposito
            print("Su deposito es ",deposito)
            suma=deposito+saldo
            print("SU SALDO ACTUAL ES: ",saldo)
    elif opciones==4:
        print("Gracias")
    break
else:
       print("opcion no valida .Por favor, elige una opcion")