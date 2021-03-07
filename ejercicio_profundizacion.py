#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
'''
import sqlite3
import numpy as np

def create_schema():
    conn = sqlite3.connect('profundizacion.db')
    c = conn.cursor()
    
    c.execute("""DROP TABLE IF EXISTS libros""")

    c.execute("""
            CREATE TABLE libros(
            [id] INTEGER PRIMARY KEY AUTOINCREMENT,
            [title] TEXT NOT NULL,
            [pags] INTEGER,
            [author] TEXT)
              """)

    conn.commit()
    conn.close()
    
def fill():
    data = np.genfromtxt('libreria.csv', delimiter=',' , dtype=None, encoding=None)
    data = data[1:,:]
    data = data.tolist()
    '''
    titulo = data[:,0]  
    titulo = titulo.tolist()
    pags = data[0:,1]
    pags = pags.tolist()
    autor = data [1:,2]
    autor = autor.tolist()
    
    '''
    
    
    conn = sqlite3.connect('profundizacion.db')
    c = conn.cursor()
    c.executemany(""" INSERT INTO libros(title, pags,author)
                values(?,?,?)""" , data)
    
    
    conn.commit()
    conn.close()
    
def fetch(id):
  conn = sqlite3.connect('profundizacion.db')
  c = conn.cursor()
  try:


    if id == 0:
      c.execute("SELECT * FROM libros")
  
    else:
        c.execute("SELECT * FROM libros WHERE  id = ? ",str(id))
  
    while True:
      row = c.fetchone()
      if row is None:
        break
      print(row)
    
  except:
    print("La linea no existe")
    
    c = conn.close()
    
def search_author(title):

    conn = sqlite3.connect('profundizacion.db')
    c = conn.cursor()

    c.execute("SELECT author FROM libros WHERE title=?" , (str(title),))
    
    while True:
      row = c.fetchone()
      if row is None:
        break
      print(row)
    
    return row

def modify(id,name):

  conn = sqlite3.connect('profundizacion.db')
  c = conn.cursor()

  c.execute("UPDATE libros SET title=? where id=?", (name,id))
  c.execute("SELECT * FROM libros")
  row = c.fetchone()

  print(row)

  conn.commit()
  conn.close()

def delete(id):

  conn = sqlite3.connect('profundizacion.db')
  c = conn.cursor()
  
  c.execute("DELETE FROM  libros where id=?", str(id))

  conn.commit()
  conn.close()


"""
Cuando finalicen el ejercicio pueden realizar las siguientes modificaciones:
- Modificar el nombre de un nombre o creando una función que utilice la sentencia UPDATE y que modifque el título de un libro según el "id" del libro deseado.
- Puedo generar una función que utilice la sentencia DELETE para borrar libros que ya no se venden en la librería por nombre del libro (título).
"""

if __name__ == "__main__":
  # Crear DB
  create_schema()

  # Completar la DB con el CSV
  fill()

  # Leer filas
  fetch(0)  # Ver todo el contenido de la DB
  fetch(3)  # Ver la fila 3
  fetch(20)  # Ver la fila 20

  # Buscar autor
  search_author('Relato de un naufrago')

  modify(1,"Hola")
  delete(2)
