from sqlalchemy import Column, Integer, String, Numeric, Boolean, Text
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime
from database import Base


class Product(Base):
    __tablename__ = "Product"
    #TODO ASIGNAR CON KF CAMPOS NECESARIOAS

    #Campos generales
    id = Column(Integer, primary_key=True, autoincrement=True)
    barcode = Column(String(50), unique=True, index=True, nullable=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=True)
    proveedor = Column(Integer, nullable=True, default=0)

    #Clasificacion
    tipo_producto = Column(Integer, nullable=False, default=1) #TODO Indice de una tabla de tipos de productos
    unidad = Column(Integer, nullable=False, default=1) #TODO Indice de una tabla unidades
    activo = Column(Boolean, nullable=False, default=True)
    maneja_inventario = Column(Boolean, nullable=False, default=True)

    #Inventariado
    stock = Column(Numeric(12, 2), nullable=False, default=0)
    stock_minimo = Column(Numeric(12, 2), nullable=False, default=0)

    #Precio y Costo
    precio_venta = Column(Numeric(12, 2), nullable=False, default=0)
    costo = Column(Numeric(12, 2), nullable=False, default=0)
    impuesto_venta = Column(Integer, nullable=True) #TODO Indice de una tabla impuestos
    impuesto_compra = Column(Integer, nullable=True) #TODO Indice de la tabla impuestos
    moneda = Column(Integer, nullable=False, default=1) #TODO Indice de una tabla monedas

    #Categoria y agrupacion
    categoria = Column(Integer, nullable=False, default=0) #TODO Indice de una tabla categorias
    referencia = Column(String(50), nullable=False, default="GNRL999") #TODO FK a tabla de referencias agrupadas

    #Control de fecha
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    fecha_actualizacion = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


