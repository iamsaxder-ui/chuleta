playlist = {}
playlist['canciones'] = []

def app():
    nombre_playlist = input('Como deseas nombrar tu playlist: \n').strip()
    while not nombre_playlist:
        nombre_playlist = input('El nombre no puede estar vacio. Como deseas nombrar tu playlist: \n').strip()
    
    playlist['nombre'] = nombre_playlist
    
    menu = True
    while menu:
        print(f"\n--- Menu de la Playlist: {playlist['nombre']} ---")
        print('1. Agregar canciones')
        print('2. Eliminar canciones')
        print('3. Actualizar una cancion')
        print('4. Mostrar resumen')
        print('5. Salir')
        
        opcion = input('Selecciona una opcion (1-5): ').strip()
        
        if opcion == '1':
            agregar_canciones()
        elif opcion == '2':
            eliminar_canciones()
        elif opcion == '3':
            actualizar_cancion()
        elif opcion == '4':
            mostrar_resumen()
        elif opcion == '5':
            print('Saliendo del programa...')
            menu = False
        else:
            print('Opcion no valida, intenta de nuevo.')

def agregar_canciones():
    print(f"\nAgregando canciones a la playlist {playlist['nombre']}")
    while True:
        cancion = input('Ingrese el nombre de la cancion (o "x" para volver al menu): ').strip()
        if cancion.lower() == 'x':
            break
        if not cancion:
            print('No puedes agregar un nombre vacio.')
            continue
        playlist['canciones'].append(cancion) 
        print(f'Cancion agregada: {cancion}')

def eliminar_canciones():
    print(f"\nEliminando cancion de la playlist {playlist['nombre']}")
    while True:
        if not playlist['canciones']:
            print('No hay canciones en la playlist para eliminar.')
            break

        cancion_eliminar = input('Ingrese el nombre de la cancion (o "x" para volver al menu): ').strip()
        if cancion_eliminar.lower() == 'x':
            break

        cancion_encontrada = None
        for cancion in playlist['canciones']:
            if cancion.lower() == cancion_eliminar.lower():
                cancion_encontrada = cancion
                break

        if cancion_encontrada:
            playlist['canciones'].remove(cancion_encontrada)
            print(f'Cancion eliminada: {cancion_encontrada}')
        else:
            print('La cancion no se pudo eliminar (no existe en la lista).')

def actualizar_cancion():
    print(f"\nActualizando cancion de la playlist {playlist['nombre']}")
    while True:
        if not playlist['canciones']:
            print('No hay canciones en la playlist para actualizar.')
            break

        cancion_actual = input('Ingrese el nombre de la cancion que desea modificar (o "x" para volver al menu): ').strip()
        if cancion_actual.lower() == 'x':
            break

        indice_encontrado = None
        for i, cancion in enumerate(playlist['canciones']):
            if cancion.lower() == cancion_actual.lower():
                indice_encontrado = i
                break

        if indice_encontrado is not None:
            nueva_cancion = input(f'Ingrese el nuevo nombre para "{playlist["canciones"][indice_encontrado]}": ').strip()
            if nueva_cancion:
                cancion_anterior = playlist['canciones'][indice_encontrado]
                playlist['canciones'][indice_encontrado] = nueva_cancion
                print(f'Cancion actualizada: "{cancion_anterior}" ahora es "{nueva_cancion}".')
                break
            else:
                print('El nuevo nombre no puede estar vacio.')
        else:
            print('La cancion no existe en la lista.')

def mostrar_resumen():
    print(f"\nPlaylist: {playlist['nombre']}")
    print('Canciones de la playlist:')
    if not playlist['canciones']:
        print('(Lista vacia)')
    else:
        for cancion in playlist['canciones']:
            print(f'- {cancion}')

app()