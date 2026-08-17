from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from database import engine, get_db, Base
from models import Student
from schemas import StudentCreate, StudentResponse, StudentUpdate

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Student Management System API",
    description="A simple REST API for managing students",
    version="1.0.0"
)


# ============= CREATE ENDPOINT =============
@app.post(
    "/create-student/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"],
    summary="Create a new student"
)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student in the database.
    
    - **name**: Student's full name (required)
    - **email**: Student's email (must be unique)
    - **age**: Student's age (must be positive)
    - **course**: Enrolled course name (required)
    """
    try:
        # Check if email already exists
        existing_student = db.query(Student).filter(Student.email == student.email).first()
        if existing_student:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email '{student.email}' already registered"
            )
        
        db_student = Student(**student.dict())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists in database"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating student: {str(e)}"
        )


# ============= READ ALL ENDPOINT =============
@app.get(
    "/students-all/",
    response_model=List[StudentResponse],
    tags=["Students"],
    summary="Get all students"
)
def get_all_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve all students from the database with pagination support.
    
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Maximum number of records to return (default: 100)
    """
    students = db.query(Student).offset(skip).limit(limit).all()
    return students


# ============= READ SINGLE ENDPOINT =============
@app.get(
    "/student/{student_id}",
    response_model=StudentResponse,
    tags=["Students"],
    summary="Get student by ID"
)
def get_student(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific student by their ID.
    
    - **student_id**: The unique identifier of the student
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    
    return student


# ============= UPDATE ENDPOINT =============
@app.put(
    "/update-students/{student_id}",
    response_model=StudentResponse,
    tags=["Students"],
    summary="Update student by ID"
)
def update_student(
    student_id: int,
    student_update: StudentUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a student's information.
    
    - **student_id**: The unique identifier of the student
    - **name**: Student's name (optional)
    - **email**: Student's email (optional, must be unique)
    - **age**: Student's age (optional, must be positive)
    - **course**: Enrolled course (optional)
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    
    # Check if new email already exists (and it's different from current email)
    if student_update.email and student_update.email != student.email:
        existing_email = db.query(Student).filter(
            Student.email == student_update.email
        ).first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email '{student_update.email}' already in use"
            )
    
    try:
        # Update only provided fields
        update_data = student_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            if value is not None:
                setattr(student, field, value)
        
        db.add(student)
        db.commit()
        db.refresh(student)
        return student
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating student: {str(e)}"
        )


# ============= DELETE ENDPOINT =============
@app.delete(
    "/delete-students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Students"],
    summary="Delete student by ID"
)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """
    Delete a student from the database.
    
    - **student_id**: The unique identifier of the student
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    
    try:
        db.delete(student)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting student: {str(e)}"
        )


# ============= HEALTH CHECK ENDPOINT =============
@app.get(
    "/health/",
    tags=["Health"],
    summary="API Health Check"
)
def health_check():
    """Check if the API is running"""
    return {"status": "OK", "message": "Student Management API is running"}


# ============= ROOT ENDPOINT =============
@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to Student Management System API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
