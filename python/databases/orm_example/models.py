from dataclasses import dataclass
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (
    DeclarativeBase, mapped_column, Mapped, relationship
)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class Product(Base):
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    category_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("categories.id", ondelete="SET NULL"))
    category: Mapped["Category"] = relationship(back_populates="products")


class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column(String(255), unique=True)
    products: Mapped[List["Product"]] = relationship(
        back_populates="category")
