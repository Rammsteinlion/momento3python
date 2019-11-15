import sqlite3

conexion = sqlite3.connect("estudiante.db")
cursor = conexion.cursor()


#--CREAR  UNA TABLA
#cursor.execute('''
 #CREATE TABLE estudiante (
#	id VARCHAR(9) PRIMARY KEY,
#	nombre VARCHAR(100),
#	apellido VARCHAR(100),
#	cedula INTEGER,
#	telefono INTEGER

#	)
#''')

#estudiante =[
#(11,'elkin','mur',52,000),
##(22,'sara','mtoro',92,000),
#(33,'andres','rodrigues',99,100),
#]
#cursor.executemany("INSERT INTO estudiante VALUES (?,?,?,?)",estudiante)

#INSERTAR UN ESTUDIANTE
#cursor.execute("INSERT INTO estudiante VALUES (34,'elkin','murillo',1123,651712)")

#--VER LISTA DE ESTUDIANTES
#cursor.execute("SELECT * FROM estudiante")
#estudiante = cursor.fetchall()
#for estudiante in estudiante:
	#print(estudiante)

#

#--Mostrar Estudiantes
#cursor.execute("SELECT * FROM estudiante WHERE id='33' ")
#estudiante = cursor.fetchall()
#print(estudiante)


#--Actualizar Estdiantes
#cursor.execute("UPDATE estudiante SET cedula=1155 WHERE id='33'    ")
#estudiante = cursor.fetchall()
#print(estudiante)

#--Borrar un Estudiante
cursor.execute("DELETE FROM estudiante WHERE id='33' ")

conexion.commit()
conexion.close()


