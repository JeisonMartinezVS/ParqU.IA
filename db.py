import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME

def obtener_conexion():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        if conn.is_connected():
            print(f"Conexión exitosa a la base de datos '{DB_NAME}' en el servidor '{DB_HOST}'")
            return conn
        else:
            print("La conexión a la base de datos falló")
            return None
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Ejecutar la función para probar la conexión
# conexion = obtener_conexion()

def registrar_placa(placa, tipo_vehiculo, rol):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO registro_placas (placa, tipo_vehiculo, rol) VALUES (%s, %s, %s)",
                (placa, tipo_vehiculo, rol)
            )
            conexion.commit()
            return True
        except mysql.connector.IntegrityError:
            return False
        except Error as e:
            print(f"Error al registrar la placa: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

def obtener_tipo_y_rol(placa):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT tipo_vehiculo, rol FROM registro_placas WHERE placa = %s", (placa,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado  # Devuelve una tupla (tipo_vehiculo, rol) o None
    else:
        return None