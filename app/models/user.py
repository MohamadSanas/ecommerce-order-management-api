from sqlalchemy import Nullable
from sqlalchemy import Boolean, String
from enum import Enum
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from app.database.base import TimestampMixin,Base






class UserRole(str, Enum):
    CUSTOMER= "customer"
    ADMIN = "admin"


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key = True, 
        index = True)

    email: Mapped[str] = mapped_column(
        String(255),
        unique = True,
        index = True,
        nullable = False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable = False,
    )

    full_name:Mapped[str] = mapped_column(
        String(255),
        nullable= True,
    )

    role:Mapped[str] = mapped_column(
        String(50),
        default=UserRole.CUSTOMER.value,
        nullable = False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, 
        default=True, 
        nullable=False)
    
    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email} role={self.role}>"