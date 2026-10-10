import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="clinica_samuel",
            port=3306
    
         )
        print("conexion exitosa")
        return conexion
    except mysql.connector.Error as error:
        print("error al conectar a la base de datos:", {error})
        return None
    except Exception as error:
        print("error inesperado:", {error})
        return None
    
conexion = conectar()