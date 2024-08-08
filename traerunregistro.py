import mysql.connector
import pandas as pd
from mysql.connector import Error


def fetch_single_record_to_dataframe(host, database, user, password, query):
    """Consulta un solo registro de la tabla y lo convierte en un DataFrame de pandas."""
    try:
        connection = mysql.connector.connect(
            host="195.179.238.58",
            database="u927419088_testing_sql",
            user="u927419088_admin",
            password="#Admin12345#"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")

            # Leer el dato en un DataFrame
            df = pd.read_sql(query, connection)
            return df

    except Error as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return None
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")


def export_to_csv(dataframe, file_name):
    """Exporta el DataFrame a un archivo CSV."""
    try:
        dataframe.to_csv(file_name, index=False)
        print(f"Datos exportados exitosamente a {file_name}")
    except Exception as e:
        print(f"Error al exportar a CSV: {e}")


# Ejemplo de uso
if __name__ == "__main__":
    query = "SELECT * FROM curso LIMIT 1 OFFSET 2"  # Selecciona el tercer registro (índice base 0)
    df = fetch_single_record_to_dataframe(host='localhost', database='nombre_base_datos', user='tu_usuario',
                                          password='tu_contraseña', query=query)

    if df is not None:
        export_to_csv(df, 'registro_3.csv')
