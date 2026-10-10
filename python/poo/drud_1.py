from conexion import conectar
import mysql.connector


# PASO 1: En conexion.py, revisa que conectar() tenga los datos correctos
# (host, usuario, contraseña y nombre de la base de datos) y devuelva la conexión.
def leer_registros(conexion):
    cursor = conexion.cursor()
    # PASO 2: Confirma en MySQL que exista la tabla paciente.
    cursor.execute("SELECT * FROM paciente")
    resultados = cursor.fetchall()
    for paciente in resultados:
        print(paciente)
    cursor.close()    
    
def leer_registros_medicos(conexion):
    cursor = conexion.cursor()
    # PASO 3: Confirma en MySQL que exista la tabla medico.
    cursor.execute("SELECT * FROM medico")
    resultados = cursor.fetchall()
    for medico in resultados:
        print(medico)
    cursor.close()  
    
def eliminar_paciente(conexion, id_paciente):
    cursor = conexion.cursor()
    # Usamos la tabla 'paciente' y su llave primaria 'id_paciente'
    sql = "DELETE FROM paciente WHERE id_paciente = %s"
    
    # ¡Importante la coma al final para que sea una tupla válida en mysql.connector!
    valores = (id_paciente,) 
    
    cursor.execute(sql, valores)
    conexion.commit()
    print(f"Paciente con ID {id_paciente} eliminado correctamente.")
    cursor.close()

# 1. PRIMERO creamos la conexión llamando a la función y guardándola en la variable 'conexion'
conexion = conectar()

# 2. DESPUÉS evaluamos si existe y ejecutamos la función
if conexion:
    eliminar_paciente(conexion, 12)  # Cambia el 12 por el ID que quieras borrar
    conexion.close()
