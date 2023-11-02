import time
import sys

archivo=open(sys.argv[1],"r")
def clean(fichero):
    usuario = []
    reemplazos = {"á": "a", "ú": "u", "í": "i", "é": "e", "ó": "o", "ã": "a"}

    def quitar_acentos(cadena):
        for buscar, reemplazar in reemplazos.items():
            cadena = cadena.replace(buscar, reemplazar)
        return cadena

    for x in fichero.readlines()[1:]:
        campos = x.split(",")
        apellido_completo = str(campos[0])[1:].split(" ")
        if len(apellido_completo) == 2:
            apellido1 = str(apellido_completo[0][0:2].lower())
            apellido2 = str(apellido_completo[1][0:2].lower())
            nombre = str(campos[1])[:-1].replace('"', '').split(" ")[1:]
            nom_usuario = (nombre[0].lower())
            nom_usuario = quitar_acentos(nom_usuario)

            usuario_completo = quitar_acentos(str(nom_usuario + apellido1 + apellido2))
            usuario.append(usuario_completo)
        else:
            apellido1 = str(apellido_completo[0][0:4].lower())
            nombre = str(campos[1])[:-1].replace('"', '').split(" ")[1:]
            nom_usuario = (nombre[0].lower())
            nom_usuario = quitar_acentos(nom_usuario)

            usuario_completo = quitar_acentos(str(nom_usuario + apellido1))
            usuario.append(usuario_completo)
    return usuario

user = clean(archivo)


sql_original = """
create user *nombre_usuario* identified by *contraseña* 
default tablespace USERS temporary tablespaces TEMP 
quota 100k on USERS;

grant rol_primero to *nombre_usuario*;
"""

sql_original = sql_original.replace("*contraseña*", "uno")

sql_modificado = ""

for nombre in user:
    sql_usuario = sql_original.replace("*nombre_usuario*", nombre)
    sql_modificado += sql_usuario
time.sleep(1)
with open("sql_modificado.sql", "w") as archivo_sql:
    archivo_sql.write(sql_modificado)
time.sleep(1)
print("Archivo SQL generado: sql_modificado.sql")