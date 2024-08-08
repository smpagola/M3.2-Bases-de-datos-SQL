import mysql.connector
import pandas as pd
from mysql.connector import Error


def fetch_data_to_dataframe(host, database, user, password, query):
    """Consulta los datos de la tabla y los convierte en un DataFrame de pandas."""
    try:
        connection = mysql.connector.connect(
            host="195.179.238.58",
            database="u927419088_testing_sql",
            user="u927419088_admin",
            password="#Admin12345#"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")

            # Leer los datos en un DataFrame
            df = pd.read_sql(query, connection)
            return df

    except Error as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return None
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")


def export_to_excel(dataframe, file_name):
    """Exporta el DataFrame a un archivo Excel."""
    try:
        dataframe.to_excel(file_name, index=False)
        print(f"Datos exportados exitosamente a {file_name}")
    except Exception as e:
        print(f"Error al exportar a Excel: {e}")


# Ejemplo de uso
if __name__ == "__main__":
    query = "SELECT * FROM curso"  # Ajusta esto según tu consulta
    df = fetch_data_to_dataframe(host='localhost', database='nombre_base_datos', user='tu_usuario',
                                 password='tu_contraseña', query=query)

    if df is not None:
        export_to_excel(df, 'cursos.xlsx')
