from sqlmodel import Field, SQLModel

# --- User Model for Authentication ---
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True, max_length=50)
    hashed_password: str = Field(max_length=255) # Store hashed password
    email: str | None = Field(default=None, unique=True, index=True, max_length=100)
    is_active: bool = Field(default=True) # Example: for account activation/deactivation

    class Config:
        from_attributes = True

# --- Pydantic Models for User Auth ---
class UserCreate(SQLModel):
    username: str = Field(max_length=50)
    password: str = Field(min_length=8, max_length=50) # Password validation
    email: str | None = Field(default=None, max_length=100)

class UserResponse(SQLModel):
    id: int
    username: str
    email: str | None = None
    is_active: bool

    class Config:
        from_attributes = True

class Token(SQLModel):
    access_token: str
    token_type: str