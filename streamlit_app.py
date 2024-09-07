import streamlit as st
from ui import insert_element, list_elements_button, delete_element, update_element

# import streamlit as st
# import psycopg2

# # Esta conexión se utiliza para consultas más especializadas
# def get_connection():
#     conn = psycopg2.connect(
#         host="localhost",  # Cambia esto a la dirección de tu servidor PostgreSQL
#         database="sale-system",  # Cambia esto al nombre de tu base de datos
#         user="postgres",  # Cambia esto al usuario de PostgreSQL
#         password="1234"  # Cambia esto a tu contraseña de PostgreSQL
#     )
#     return conn

# # Esta función renderiza el formulario y tiene la lógica para insertar elementos
# def insert_element():
#     # Botón para insertar datos
#     name = st.text_input("Nombre")
#     pet = st.text_input("Mascota")
#     if st.button("Insertar registro"):
#         if name and pet:
#             try:
#                 # Conecta a la base de datos
#                 conn = get_connection()
#                 cursor = conn.cursor()

#                 # Inserta los datos
#                 insert_query = "INSERT INTO mytable (name, pet) VALUES (%s, %s)"
#                 cursor.execute(insert_query, (name, pet))
                
#                 # Confirma la transacción
#                 conn.commit()
#                 list_elements(cursor, conn)
#                 st.success("Registro insertado exitosamente")
#             except Exception as e:
#                 st.error(f"Ocurrió un error: {e}")
#             finally:
#                 cursor.close()
#                 conn.close()
#         else:
#             st.warning("Por favor, completa todos los campos")

# def list_elements(cursor, conn):
#     try:
#         # Realiza la consulta para obtener todos los registros
#         select_query = "SELECT * FROM mytable"
#         cursor.execute(select_query)
#         registros = cursor.fetchall()
#         # Muestra los registros
#         if registros:
#             for registro in registros:
#                 st.write(f"Nombre: {registro[0]}, Mascota: {registro[1]}")
#         else:
#             st.write("No se encontraron registros.")

#     except Exception as e:
#         st.error(f"Ocurrió un error al listar los registros: {e}")

# def list_elements_button():
#     if st.button("Listar registros"):
#         try:
#             conn = get_connection()
#             cursor = conn.cursor()
#             # Realiza la consulta para obtener todos los registros
#             select_query = "SELECT * FROM mytable"
#             cursor.execute(select_query)
#             registros = cursor.fetchall()
#             # Muestra los registros
#             if registros:
#                 for registro in registros:
#                     st.write(f"Nombre: {registro[0]}, Mascota: {registro[1]}")
#             else:
#                 st.write("No se encontraron registros.")

#         except Exception as e:
#             st.error(f"Ocurrió un error al listar los registros: {e}")
#         finally:
#             cursor.close()
#             conn.close()
            
# # Función para eliminar un registro por nombre
# def delete_element():
#     # Solicitar el nombre del registro a eliminar
#     name_to_delete = st.text_input("Nombre del registro a eliminar")
#     if st.button("Eliminar registro"):
#         if name_to_delete:
#             try:
#                 # Conectar a la base de datos
#                 conn = get_connection()
#                 cursor = conn.cursor()

#                 # Eliminar el registro de la tabla
#                 delete_query = "DELETE FROM mytable WHERE name = %s"
#                 cursor.execute(delete_query, (name_to_delete,))
                
#                 # Confirmar la transacción
#                 conn.commit()
                
#                 # Verificar si se eliminó algún registro
#                 if cursor.rowcount > 0:
#                     st.success("Registro eliminado exitosamente")
#                 else:
#                     st.warning("No se encontró un registro con ese nombre.")
                
#                 # Mostrar los registros actualizados
#                 list_elements(cursor, conn)

#             except Exception as e:
#                 st.error(f"Ocurrió un error al eliminar el registro: {e}")
#             finally:
#                 cursor.close()
#                 conn.close()
#         else:
#             st.warning("Por favor, ingresa el nombre del registro a eliminar")

# # Función para actualizar un registro
# def update_element():
#     # Solicitar el nombre del registro que deseas actualizar
#     name_to_update = st.text_input("Nombre del registro a actualizar")
    
#     # Solicitar nuevos datos para actualizar
#     new_name = st.text_input("Nuevo nombre")
#     new_pet = st.text_input("Nueva mascota")
    
#     # Botón para ejecutar la actualización
#     if st.button("Actualizar registro"):
#         if name_to_update and new_name and new_pet:
#             try:
#                 # Conectar a la base de datos
#                 conn = get_connection()
#                 cursor = conn.cursor()

#                 # Actualizar los datos del registro
#                 update_query = "UPDATE mytable SET name = %s, pet = %s WHERE name = %s"
#                 cursor.execute(update_query, (new_name, new_pet, name_to_update))
                
#                 # Confirmar la transacción
#                 conn.commit()
                
#                 # Verificar si se actualizó algún registro
#                 if cursor.rowcount > 0:
#                     st.success("Registro actualizado exitosamente")
#                 else:
#                     st.warning("No se encontró un registro con ese nombre.")
                
#                 # Mostrar los registros actualizados
#                 list_elements(cursor, conn)

#             except Exception as e:
#                 st.error(f"Ocurrió un error al actualizar el registro: {e}")
#             finally:
#                 cursor.close()
#                 conn.close()
#         else:
#             st.warning("Por favor, completa todos los campos")

# # Función inicial, se encarga de orquestar la app indicando qué métodos se deben renderizar
# def init_app():
#     st.write("Insertar")
#     insert_element()  # Formulario para insertar elementos
#     st.write("Listar")
#     list_elements_button()
#     st.write("eliminar")
#     delete_element()
#     st.write("actualizar")
#     update_element() 

# Función inicial para organizar las funcionalidades
def init_app():
    st.title("🎈 My new app")
    insert_element()  # Formulario para insertar elementos
    st.write("---")
    list_elements_button()  # Botón para listar elementos
    st.write("---")
    delete_element()  # Formulario para eliminar un registro
    st.write("---")
    update_element()  # Formulario para actualizar un registro

# Ejecuta la aplicación
if __name__ == "__main__":
    init_app()