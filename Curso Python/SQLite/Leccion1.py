import sqlite3

conexion = sqlite3.connect("ejemplo.db")#base de datos creada

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
#cursor.execute("INSERT INTO usuarios VALUES ('Hector',27,'hector@ejemplo.com')")
# cursor.execute("SELECT * FROM usuarios")
# usuario = cursor.fetchone()
# print(usuario[0])

# usuarios = [
#     ('Mario', 51, "mario@ejemplo.com"),
#     ('Juan', 38, "juan@ejemplo.com"),
#     ('Letz', 27, "mario@ejemplo.com")
# ]

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

for usuario in usuarios:
    print("Nombre: ",usuario[0], " - Email: ",usuario[2])

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)


conexion.commit()

conexion.close()