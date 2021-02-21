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
    row = c.fetchall()
    
    conn.commit()
    conn.close()
    
    

if __name__ == "__main__":
  # Crear DB
  create_schema()

  # Completar la DB con el CSV
  fill()

  # Leer filas
  #fetch()  # Ver todo el contenido de la DB
  #fetch(3)  # Ver la fila 3
  #fetch(20)  # Ver la fila 20

  # Buscar autor
  #print(search_author('Relato de un naufrago'))