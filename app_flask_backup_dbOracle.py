
#import getpass

#import oracledb

#un = 'scott'#nuestro nombre de usuario 
#cs = 'localhost/orclpdb'#nuestra de cadena de conexion
#pw = getpass.getpass(f'Enter password for {un}@{cs}: ')

#with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
#    with connection.cursor() as cursor:
#        sql = """select sysdate from dual"""
#        for r in cursor.execute(sql):
#            print(r)
from app_models_oracle import cx_Oracle
import subprocess

def ejecutar_rman_backup(usuario, contrasena, host, puerto, sid, directorio_copia_seguridad):
    try:
        conexion = cx_Oracle.connect(f"{usuario}/{contrasena}@{host}:{puerto}/{sid}")
        conexion.close()
        
        directory_copia_seguridad = "user_boss/2024/localhost:1521/ORCL"
        # Construir el comando RMAN
        rman_comando = f"rman target {usuario}/{contrasena}@{host}:{puerto}/{sid}"
        # Comando para la copia de seguridad de la base de datos completa
        rman_backup_comando = f"BACKUP FULL DATABASE {directory_copia_seguridad}"
            # Ejecutar el comando RMAN a través de subprocess
        result = subprocess.run([rman_comando, rman_backup_comando], capture_output=True, text=True, check=True)
            
        print(result.stdout) # Imprimir la salida de RMAN
            
        return result.stdout

    except cx_Oracle.Error as err:
        print(f"Error de conexión: {err}")
        return None
    except subprocess.CalledProcessError as err:
            print(f"Error al ejecutar RMAN: {err}")
            return None