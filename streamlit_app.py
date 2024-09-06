import streamlit as st
import psycopg2

# Esta conexión se utiliza para consultas más especializadas
def get_connection():
    conn = psycopg2.connect(
        host="localhost",  # Cambia esto a la dirección de tu servidor PostgreSQL
        database="sale-system",  # Cambia esto al nombre de tu base de datos
        user="postgres",  # Cambia esto al usuario de PostgreSQL
        password="1234"  # Cambia esto a tu contraseña de PostgreSQL
    )
    return conn

# Esta función renderiza el formulario y tiene la lógica para insertar elementos
def insert_element():
    # Botón para insertar datos
    name = st.text_input("Nombre")
    pet = st.text_input("Mascota")
    if st.button("Insertar registro"):
        if name and pet:
            try:
                # Conecta a la base de datos
                conn = get_connection()
                cursor = conn.cursor()

                # Inserta los datos
                insert_query = "INSERT INTO mytable (name, pet) VALUES (%s, %s)"
                cursor.execute(insert_query, (name, pet))
                
                # Confirma la transacción
                conn.commit()
                
                st.success("Registro insertado exitosamente")
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            st.warning("Por favor, completa todos los campos")

# Esta función se encarga de listar los registros de la tabla 'mytable'
def list_elements():
    if st.button("Listar registros"):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Realiza la consulta para obtener todos los registros
            select_query = "SELECT * FROM mytable"
            cursor.execute(select_query)
            registros = cursor.fetchall()
            # Muestra los registros
            if registros:
                for registro in registros:
                    st.write(f"Nombre: {registro[0]}, Mascota: {registro[1]}")
            else:
                st.write("No se encontraron registros.")

        except Exception as e:
            st.error(f"Ocurrió un error al listar los registros: {e}")
        finally:
            cursor.close()
            conn.close()

# Función inicial, se encarga de orquestar la app indicando qué métodos se deben renderizar
def init_app():
    insert_element()  # Formulario para insertar elementos
    st.write("---")
    list_elements()  # Funcionalidad para listar los registros

# Ejecuta las consultas cuando se inicia la aplicación
if __name__ == "__main__":
    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )
    init_app()
