from unicodedata import category
from sqlalchemy import Numeric
from decimal import Decimal
from pygments.token import Text
from typing import Optional
from httpcore._exceptions import map_exceptions
from sqlalchemy.util.cython import double
from sqlalchemy import Integer,Boolean, ForeignKey,Text
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.database.base import Base,TimestampMixin
from sqlalchemy import String


class Product(Base,TimestampMixin):
    __tablename__ = "products"

    id:Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name:Mapped[str] = mapped_column(
        String(255),
        nullable= False,
        unique = True,
        index=True
        
    )

    description:Mapped[Optional[str]]= mapped_column(
        Text,
        nullable = True
    )

    price:Mapped[Decimal] = mapped_column(
        Numeric(10,2),
        nullable=False
    )

    stock_quantity: Mapped[int] = mapped_column(
        Integer, 
        default=0, 
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, 
        default=True, 
        nullable=False
    )

    category_id:Mapped[int]= mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False,
        index = True
    )

    category: Mapped["Category"] = relationship("Category", back_populates="products")


    def __repr__(self) -> str:
        return f"<Product id={self.id} name={self.name} price={self.price}>"