import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute("UPDATE usuarios SET nombre ='Hector Costa WHERE dni = '11111111A'" )

# usuario = cursor.fetchchone()
# print(usuario)
cursor.execute("DELETE FROM usuarios WHERE dni='11111111A'")



conexion.commit()
conexion.close()