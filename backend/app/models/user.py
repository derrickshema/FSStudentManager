from sqlmodel import Field, SQLModel
from datetime import date, datetime, timezone

# --- User Model for Authentication ---
class UserBase(SQLModel):
    username: str = Field(max_length=50, unique=True, index=True)
    email: str | None = Field(default=None, max_length=100, unique=True, index=True)
    is_active: bool = Field(default=True)  # Example field for user status

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str = Field(max_length=255) # Store hashed password
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)}
    )

# --- Pydantic Models for User Auth ---
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=50) # Password validation

class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class Token(SQLModel):
    access_token: str
    token_type: str