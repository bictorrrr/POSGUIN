import sqlite3
import os

# Ruta al archivo de la base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), "database.db")

def obtener_productos():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT codigo, nombre, precio_venta, precio_compra, stock, activo FROM productos")
    productos = cursor.fetchall()
    
    conexion.close()
    return productos

def obtener_productos_por_nombre(nombre):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT codigo, nombre, precio_venta, precio_compra, stock, activo FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
    productos = cursor.fetchall()
    
    conexion.close()
    return productos
