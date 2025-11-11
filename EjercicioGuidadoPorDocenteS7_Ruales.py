# 1. Importar Biblioteca de conexión
import pyodbc
import json 

#2. Crear funciones 

# Función consultar registros
def consultar_registro(conexion):
    try:
        conexion = pyodbc.connect(connection_string)
        #Parámetro de Entrada
        l_IDEstudiante = int(input("\n\n\tIngrese ID del Estudiante a Consultar: \t"))
        #Crear Cursor
        micursor = conexion.cursor()
        # 1. Ejemplo: Llamar a SP para Consulta la tabla "Estudiantes”
        SENTENCIA_SQL = "{CALL sp_ListadoEstudiantes (?)}"
        micursor.execute(SENTENCIA_SQL,(l_IDEstudiante))
        
        # Obtener los resultados  
        print("\n\n\t\t\tDatos del Estudiante:")
        rows = micursor.fetchall()
        
        #if rows:
        for row in rows:
        ##print(f"\t\t{row.NombreEstudiante}\t{row.ApellidoEstudiante}\t{row.Email}")
            print(row)


    finally:
        print("\nOk ... Proceso Culminado con Exito: \n")
# Función insertar registros
def insertar_registro(conexion):
    try:
        conexion = pyodbc.connect(connection_string)
        #Crear Cursor
        micursor = conexion.cursor()
        # Ejemplo: Insertar Tabla Estudiantes 1 Registro
        
        SENTENCIA_SQL = """
        INSERT INTO Estudiantes
        (IDEstudiante,NombreEstudiante,ApellidoEstudiante,Email,Telefono)
        VALUES(?,?,?,?,?)
        """
        #one_record = ('10','Pepe','Muñoz','pepem@gmail.com','2378008')   
        #micursor.execute(SENTENCIA_SQL, one_record)
        print("\n\t\tINSERTAR NUEVO ESTUDIANTE:\n")  
        ## Ingreso de Informacion
        l_IDEstudiante = int(input("Ingrese ID del Estudiante: \t"))
        l_NombreEstudiante = input("Ingrese Nombre Estudiante: \t")
        l_ApellidoEstudiante = input("Ingrese Apellido Estudiante:\t")
        l_Email = input("Ingrese Email Estudiante: \t")
        l_Telefono = input("Ingrese Telefono Estudiante 593-xxx-xxxx:\t")   
            
        micursor.execute( SENTENCIA_SQL,(l_IDEstudiante,l_NombreEstudiante,l_ApellidoEstudiante,l_Email,l_Telefono))
        
        #Realizar Commit
        micursor.commit()
    finally:
        print("\nOk ... Insercion Exitosa: \n")        
# Función eliminar registros
def eliminar_registro(conexion):
    try:
        conexion = pyodbc.connect(connection_string)
        #Crear Cursor
        micursor = conexion.cursor()
        
        SENTENCIA_SQL = """DELETE FROM Estudiantes
        WHERE IDEstudiante=?"""
        ## Ingreso de Informacion
        print("\n\t Eliminar Registro Estudiante:\n")
        l_IDEstudiante = int(input("Ingrese ID del Estudiante a Elimnar: \t"))
        
        micursor.execute( SENTENCIA_SQL,(l_IDEstudiante))
        micursor.commit()   
    finally:
        print("Ok ... Eliminacion Exitosa: \n")

# Función actualizar registros
def actualizar_registro(conexion):
    try:
        conexion = pyodbc.connect(connection_string)    
        #Crear Cursor
        micursor = conexion.cursor()
        
        SENTENCIA_SQL = """UPDATE Estudiantes
        SET Email = ?
        WHERE IDEstudiante= ?"""
        ## Ingreso de Informacion
        print("\n\t Actualizar Informacion Estudiante:\n")
        l_IDEstudiante = int(input("Ingrese ID del Estudiante: \t"))
        l_Email = input("Ingrese Nuevo E-Mail Estudiante: \t")
        micursor.execute( SENTENCIA_SQL,(l_Email,l_IDEstudiante))
        
        micursor.commit()
    finally:
        print("\nOk ... Actualización Exitosa: \n")   
# Función mostrar opciones
def mostrar_opciones_crud():
    print("\t****************************")  
    print("\t** SISTEMA CRUD UDEMYTEST **")  
    print("\t****************************")  
    print("\tOpciones CRUD:\n")
    print("\t1. Crear registro")
    print("\t2. Consultar registros")
    print("\t3. Actualizar registro")
    print("\t4. Eliminar registro")
    print("\t5. Salir\n\n")


    
# 3. Declarar variables de Conexión
with open('config.json') as archivo_config:
    config = json.load(archivo_config)
    
name_server = config["sql_server"]["name_server"]
database = config["sql_server"]["database"]
username = config["sql_server"]["username"]
password = config["sql_server"]["password"]
controlador_odbc = config["sql_server"]["controlador_odbc"]

connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'


#4. Establece la conexión
try:
    conexion = pyodbc.connect(connection_string) 
except Exception as e:
    print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)    
# Fin Conexion de BDD
else:  
    
    
    while True:
        mostrar_opciones_crud()
        opcion = input("Seleccione una opción 1-5:\t")
        
        if opcion == '1':
            #crear_registro(conexion)
            insertar_registro(conexion)
        elif opcion == '2':
            #leer_registros(conexion)
            consultar_registro(conexion)
        elif opcion == '3':
            actualizar_registro(conexion)
        elif opcion == '4':
            eliminar_registro(conexion)
        elif opcion == '5':
            print("Saliendo del programa...")
            conexion.close()
            break
        else:
            print("Opción no válida. Ingrese un numero de 1-5")        
    
finally:
    print("Conexion Cerrada: \n")
