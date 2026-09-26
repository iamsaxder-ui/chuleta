#while

contador = -1
while contador <=12:
        contador += 1
        if contador ==2:
            print("diego le gusta maycol jakson")
            continue
        if contador ==5:
            print("sebastina le gusta el keke")
            continue
        if contador ==8:
            print("eyla odia las motos")    
            break
        print(contador)
else:
    print("buvle completado sin interar")

    
    
password = ""
while len(password)<8:
    password = input("ingresa una clave de minimo 8 caracteres")
    if len(password)<8:
         print("error en la longitud es insuficiente. intentalo de nuevo")
print("contrasena aceptada correctamente")