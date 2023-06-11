disponible = 4500
intentos = 3
print('**** bienvenido a nequi **** ')
while intentos >0:
    numero = int(input(" por favor ingrese el numero de celular registrado \n "))
    contraseña = int(input("ingrese la clave \n "))
    if numero == 3105185564 and contraseña == 1030:
        print(' **** bienvenido a tu nequi **** ')
        print(f'** Tu saldo Disponible es {disponible} ** ')
        break

    intentos=intentos-1
    print(f' ¡Upps! Parece que tus datos de acceso no son correctos  ')
        
        
    if intentos > 0 :
        print(f'Tienes {intentos} intentos más')
        
    else :
        print('no tienes mas intentos')
        exit()
while True :
    
    opcion = int(input("ingrese la opcion a  \n\
                1. Saca \n\ 2. Envia \n\ 3. Recarga \n\ 4. salir    \n "))
    if opcion == 1:
        opcion = int(input("ingrese la opcion a  \n\
            1. Cajero \n\ 2. Punto fisico \n "))
        if disponible < 2000:
            print('no te alcanza')
        elif disponible >2000 :
            retiro = int(input('cuanto de sea retirar \n'))
            disponible=disponible-retiro
            print('Tu codigo de retiro es 25478547')
            print(f'Tu saldo actual es {disponible} ')
    if opcion == 2:
        input('ingrese el numero de telefono al cual desea realizar el envio \n')
        envio = int(input('ingrese el valor a enviar \n '))
        if envio > disponible:
            print('no es posible enviar el dinero')
        else:
            disponible = disponible-envio
            print(f'Tu Saldo Disponible Ahora es {disponible}')
    if opcion == 3:
        recarga = int(input("Ingrese el valor a recargar \n"))
        disponible = disponible-recarga
        confirmar = int (input("Desea confirmar su recarga  \n\
            1. si deseo confirmar \n\
            2. no deseo confirmar \n "))
        if disponible < 0 and confirmar == 1:
            print('fondos insuficientes')
        elif  disponible > 0 and confirmar == 1:    
            print(f'Su recarga fue realizada correctamente su nuevo saldo es {disponible} ')
    elif confirmar == 2:
            print('gracias por su visita')                    
    else:
        print('')
    if opcion == 4:
            print('Adios vuelve pronto')

    input("ingrese la opcion a  \n\
    si. continuar \n\
    no. salir   ")