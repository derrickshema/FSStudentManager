from sqlmodel import SQLModel, Field
from datetime import date, datetime, timezone

# Base model for Student (Shared fields)
class StudentBase(SQLModel):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    enrollment_date: date
    grade_level: str
    major: str | None = None
    gpa: float | None = None
    status: str = "Active"

# Table model (DB only)
class Student(StudentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=datetime.now(timezone.utc), sa_column_kwargs={"onupdate": datetime.now(timezone.utc)})

# Request model/schema for creating a new student
class StudentCreate(StudentBase):
    pass

# Response model/schema for returning student data
class StudentRead(StudentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLModel

# Update model/schema for updating an existing student
class StudentUpdate(SQLModel):
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None
    enrollment_date: date | None = None
    grade_level: str | None = None
    major: str | None = None
    gpa: float | None = None
    status: str | None = None
