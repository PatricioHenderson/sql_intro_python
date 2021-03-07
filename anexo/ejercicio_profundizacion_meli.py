import sqlite3
import csv
import json
import requests

def create_schema():
  conn = sqlite3.connect('meli.db')
  c = conn.cursor()

  c.execute('''
            DROP TABLE IF EXISTS productos;
            ''')
  
  c.execute('''
            CREATE TABLE  productos(

              [id] ,
              [site_id] ,
              [title] ,
              [price] ,
              [currency_id] 
              [initial_quantity] ,
              [available_quantity] ,
              [sold_quantity]  
            );

            ''')
  conn.commit()
  conn.close()


def fill():
  
  conn = sqlite3.connect('meli.db')
  c = conn.cursor()
  with open ('technical_challenge_data.csv' , 'r') as fo:
    data = csv.DictReader(fo)
    for i in data:
      
      url = 'https://api.mercadolibre.com/items?ids={}{}'.format(i['site'],i['id'])
      response = requests.get(url)
      datas = json.loads(response.text)
      datas = response.json()
      filter_data =  [datas[0]['body']]
      try:
        for x in filter_data:
        
          c.execute("""INSERT INTO productos(id,site_id,title,price,currency_id,initial_quantity,available_quantity,sold_quantity)
                 VALUES(?,?,?,?,?,?,?,?)""" , (x['id'],x['site_id'], x['title'],x['price'],x['currency_id'],x['initial_quantity'],x['available_quantity'],x['sold_quantity'],))
          
          conn.commit()
      except:
        pass
  
  conn.close()

def fetch(id):
  conn = sqlite3.connect('meli.db')
  c = conn.cursor()
  try:
    c.execute('''SELECT * FROM productos WHERE id = ? ''' , id )
  except:
    print('Error 404')
  conn.commit()
  conn.close()


if __name__ == "__main__":
  # Crear DB
  create_schema()

  # Completar la DB con el CSV
  fill()

  # Leer filas
  fetch('MLA845041373')
  fetch('MLA717159516')

