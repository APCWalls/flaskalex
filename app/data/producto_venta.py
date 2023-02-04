
from app.data.modelo.producto import Producto

class ProductoVenta:

    def select_all(self,db) -> list[Producto]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM producto')
        productos_en_db = cursor.fetchall()
        productos : list[Producto]= list()
        for producto_en_db in productos_en_db:
            productos.append(Producto(producto_en_db[0], producto_en_db[1], producto_en_db[2], producto_en_db[3]))
        cursor.close()
        return productos

    #def insertar(self,db,producto:Producto) -> bool:
    #    cursor = db.cursor()
     #   cursor.execute('INSERT INTO producto ',(producto.id,producto.nombre))
        
  
      #  cursor.close()
       # return productos        