# app/routers/product.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductRead

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductRead)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    if product.barcode:
        exists = db.query(Product).filter(Product.barcode == product.barcode).first()
        if exists:
            raise HTTPException(status_code=400, detail="Barcode ya existe")
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductRead])
def list_products(
        db: Session = Depends(get_db),
        q: Optional[str] = None,
        activos: Optional[bool] = None,
):
    query = db.query(Product)
    if q:
        like = f"%{q}%"
        query = query.filter(Product.nombre.ilike(like))
    if activos is not None:
        query = query.filter(Product.activo == activos)
    return query.order_by(Product.id.desc()).all()

@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    prod = db.query(Product).get(product_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod

@router.put("/{product_id}", response_model=ProductRead)
def update_product(product_id: int, data: ProductCreate, db: Session = Depends(get_db)):
    prod = db.query(Product).get(product_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for k, v in data.dict().items():
        setattr(prod, k, v)
    db.commit()
    db.refresh(prod)
    return prod

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    prod = db.query(Product).get(product_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(prod)
    db.commit()
    return {"ok": True}
