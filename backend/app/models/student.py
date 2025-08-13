from sqlmodel import SQLModel, Field
from datetime import date, datetime, timezone
from typing import Optional

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    enrollment_date: date
    grade_level: str
    major: Optional[str] = None
    gpa: Optional[float] = None
    status: str = "Active"
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=datetime.now(timezone.utc), sa_column_kwargs={"onupdate": datetime.now(timezone.utc)})
