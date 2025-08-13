from sqlmodel import SQLModel, Field, Session, select
from fastapi import APIRouter, Depends, HTTPException, status

from ..models.user import User
from ..routes.auth_routes import get_current_user

from ..db.session import get_session
from ..models.student import Student
router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student(student: Student, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    """
    Creates a new student in the database.
    """
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@router.get("/", response_model=list[Student])
async def get_students(session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    """
    Fetches all students from the database.
    """
    students = session.exec(select(Student)).all()
    return students

@router.get("/{student_id}", response_model=Student)
async def get_student(student_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    """
    Fetches a student by ID from the database.
    """
    student = session.exec(select(Student).where(Student.id == student_id)).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=Student)
async def update_student(student_id: int, updated_student: Student, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    """
    Updates a student's information in the database.
    """
    existing_student = session.exec(select(Student).where(Student.id == student_id)).first()
    if not existing_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    for key, value in updated_student.model_dump(exclude_unset=True).items():
        setattr(existing_student, key, value)

    session.add(existing_student)
    session.commit()
    session.refresh(existing_student)
    return existing_student

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    """
    Deletes a student by ID from the database.
    """
    student = session.exec(select(Student).where(Student.id == student_id)).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    session.delete(student)
    session.commit()
    return {"detail": "Student deleted successfully"}