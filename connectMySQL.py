import mysql.connector
from mysql.connector import Error

def connect_to_mysql(host, database, user, password):
    """Establece una conexión con la base de datos MySQL"""
    try:
        connection = mysql.connector.connect(
            host="195.179.238.58",
            database="u927419088_testing_sql",
            user="u927419088_admin",
            password="#Admin12345#"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            # Ejecutar una consulta simple, por ejemplo, obtener la versión de MySQL
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Conectado a la base de datos: {record}")
            cursor.close()
    except Error as e:
        print(f"Error al conectarse a la base de datos: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")

# Ejemplo de uso
if __name__ == "__main__":
    connect_to_mysql(host='localhost', database='nombre_base_datos', user='tu_usuario', password='tu_contraseña')
