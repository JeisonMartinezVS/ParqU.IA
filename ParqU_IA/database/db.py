import reflex as rx
import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='placas_db'
        )
        if conn.is_connected():
            print(f"Conexión exitosa a la base de datos")
            return conn
        else:
            print("La conexión a la base de datos falló")
            return None
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def registrar_placas(nombre, placa, tipo_vehiculo, rol):
    connec = obtener_conexion()
    if connec is None:
        return "Error de conexion con la base de datos"
    try:
        cursor = connec.cursor()
        query = "INSERT INTO registro_placas (nombre, placa, tipo_vehiculo, rol) VALUES (%s, %s, %s, %s)"
        value = (nombre, placa, tipo_vehiculo, rol)
        cursor.execute(query, value)
        connec.commit()
        return "Usuario Registrado"
    
    except Error as e:
        return f"Error al registrar el usuario: {e}"
    
    finally:
        if connec.is_connected():
            cursor.close()
            connec.close()
            
def obtener_usuarios():
    connec = obtener_conexion()
    cursor = connec.cursor()
    
    try:
        cursor.execute(
            'SELECT nombre, placa, tipo_vehiculo, rol FROM registro_placas'
        )
        users = cursor.fetchall()
        
        list_users = [
            {"nombre": user[0] ,"placa": user[1], "tipo_vehiculo": user[2], "rol": user[3]}
            for user in users
        ]
        
        return list_users

    except Exception as e:
        print(f"Error al obtener la lista de usuarios: {e}")
        return []
    
    finally:
        cursor.close()
        connec.close()
