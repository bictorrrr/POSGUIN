# app/schemas/product.py (Pydantic v2)
from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    barcode: Optional[str] = Field(default=None)
    nombre: str
    descripcion: Optional[str] = Field(default=None)
    proveedor: Optional[int] = Field(default=0)

    tipo_producto: int = Field(default=1)
    unidad: int = Field(default=1)
    activo: bool = Field(default=True)
    maneja_inventario: bool = Field(default=True)

    stock: float = Field(default=0, ge=0)
    stock_minimo: float = Field(default=0, ge=0)

    precio_venta: float = Field(ge=0)
    costo: Optional[float] = Field(default=None, ge=0)
    impuesto_venta: Optional[int] = Field(default=None, ge=0)
    impuesto_compra: Optional[int] = Field(default=None, ge=0)
    moneda: int = Field(default=0)

    categoria: int = Field(default=0)
    referencia: str = Field(default="GNRL999")

    model_config = {
        "from_attributes": True,      # reemplaza orm_mode de v1
        "populate_by_name": True,     # permite mandar/recibir camelCase o snake_case
    }

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
