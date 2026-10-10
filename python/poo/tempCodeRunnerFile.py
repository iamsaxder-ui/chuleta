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
    
def eliminar_especialidad(conexion, id_especialidad):    
    cursor = conexion.cursor()
    # PASO 4: Verifica que la columna se llame id. Esta consulta borra datos
    # definitivamente; comprueba el ID antes de ejecutar esta función.
    sql = "DELETE FROM especialidad WHERE id = %s"
    valores = (id_especialidad )
    cursor.execute(sql, valores)
    conexion.commit()
    print("especialidad eliminada correctamente.")
    cursor.close()

# PASO 5: Inicia MySQL desde Laragon y ejecuta este archivo con Python.
conexion = conectar()

if conexion:
    # PASO 6: Se muestran ambas tablas y luego se elimina el paciente con ID 4.
    # Cambia el 4 por el ID correcto o comenta la línea si no quieres borrar.
    leer_registros(conexion)  
    leer_registros_medicos(conexion)      
    eliminar_especialidad(conexion, 1) 
