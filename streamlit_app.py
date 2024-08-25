import streamlit as st
import psycopg2

# Función para inicializar la conexión a ala base de datos
def initialize_connection():
    try:
        st.write("Initializing connection...")
        conn = st.connection("postgresql", type="sql")
        st.success("Connection successfully established!")
        return conn
    except Exception as e:
        st.error(f"An error occurred while initializing the connection: {e}")
        return None

# Función para realizar una consulta
def execute_query(query, conn):
    try:
        df = conn.query(query, ttl="10m")
        st.dataframe(df)
    except Exception as e:
        st.error(f"An error occurred while executing the query: {e}")

# Función para realizar múltiples consultas
def get_elements():
    # Inicializa la conexión
    conn = initialize_connection()    
    if conn is not None:
            # Consulta 1
            query1 = 'SELECT * FROM mytable;'
            execute_query(query1, conn)

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

# función inical, se encarga de orquestar la app indicando que metodos se deben renderizar desde el inicio
def init_app():
    insert_element()
    get_elements()
    
# Ejecuta las consultas cuando se inicia la aplicación
if __name__ == "__main__":
    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )
    init_app()

