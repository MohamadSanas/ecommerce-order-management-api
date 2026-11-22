from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String , Text
from  app.database.base import Base,TimestampMixin
from typing import Optional, List


class Category(Base,TimestampMixin):

    __tablename__ = "categories"

    id:Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name:Mapped[str] = mapped_column(
        String(100),
        nullable = False,
        unique = True
    )

    slug: Mapped[str] = mapped_column(
        String(100), 
        unique=True, 
        index=True, 
        nullable=False
        )
    description: Mapped[Optional[str]] = mapped_column(
        Text, 
        nullable=True
        )

    products:Mapped[List["Product"]] = relationship(
        "Product", back_populates = "category",
        cascade = "all,delete-orphan"
    )


    def __repr__(self) -> str : return f"<Category id={self.id} name={self.name}>"