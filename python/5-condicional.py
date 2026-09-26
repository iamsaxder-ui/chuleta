# En la condicional se debe declarar la variable antes de la condicional

edad = 20
if edad > 18:
    print("es mayor de edad, puedes tomar")
else:
    print("no puedes tomar, no eres mayor de edad")

user = 'saxder'
password = '123'
rol_user = 'profesor'
rol_users = ['admin', 'estudiante', 'invitado', 'profesor']

if user == 'saxder' and rol_user in rol_users:
    if rol_user == 'admin':
        print('tienes ACCESO COMPLETO')
    elif rol_user == 'estudiante':
        print('el usuario es estudiante')
    elif rol_user == 'profesor':
        print('el usuario es profesor')
    else:
        print('el usuario es invitado')
else:
    print('el usuario no puede entrar al sistema')


tipo = 'estudiante'

if tipo == 'estudiante':
    print('tienes un descuento del 20%')
elif tipo == 'profesor':
    print('tienes un descuento del 10%')
else:
    print('no tienes descuento')


