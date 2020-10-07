import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

# cursor.execute(''' 
#     CREATE TABLE usuarios(
#         dni VARCHAR(9) PRIMARY KEY,
#         nombre VARCHAR(100),
#         EDAD INTEGER,
#         EMAIL VARCHAR(100)
#     )
#     ''')

# usuarios = [
#     ('11111111A','Hector', 27, "hector@ejemplo.com"),
#     ('22222222B','Mario', 51, "mario@ejemplo.com"),
#     ('33333333C','Juan', 38, "juan@ejemplo.com"),
#     ('44444444D','Letz', 27, "mario@ejemplo.com")
# ]

#cursor.executemany("INSERT INTO usuarios VALUES(?,?,?,?)", usuarios)

#cursor.execute("INSERT INTO usuarios VALUES('55555555E','Letz', 27, 'mario@ejemplo.com')")

# cursor.execute('''
#     CREATE TABLE productos1(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#         )
#     ''')


# productos = [
#     ('Teclado', 'Logitech', 19.95),
#     ('Pantalla 19','LG', 89.95)
# ]

# cursor.executemany("INSERT INTO productos1 VALUES(null,?,?,?)", productos)

# cursor.execute("SELECT * FROM productos1")

# productos = cursor.fetchall()
# for producto in productos:
#     print (producto)

conexion.commit()
conexion.close()