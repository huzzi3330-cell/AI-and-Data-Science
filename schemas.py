from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class StudentBase(BaseModel):
    """Base student schema with common fields"""
    name: str
    email: EmailStr
    age: int
    course: str

    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        if len(v) > 100:
            raise ValueError('Name must be less than 100 characters')
        return v.strip()

    @field_validator('age')
    @classmethod
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Age must be positive')
        if v > 120:
            raise ValueError('Age cannot exceed 120')
        return v

    @field_validator('course')
    @classmethod
    def course_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Course cannot be empty')
        if len(v) > 100:
            raise ValueError('Course must be less than 100 characters')
        return v.strip()


class StudentCreate(StudentBase):
    """Schema for creating a student"""
    pass


class StudentUpdate(BaseModel):
    """Schema for updating a student (all fields optional)"""
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    course: Optional[str] = None

    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v):
        if v is not None:
            if not v.strip():
                raise ValueError('Name cannot be empty')
            if len(v) > 100:
                raise ValueError('Name must be less than 100 characters')
            return v.strip()
        return v

    @field_validator('age')
    @classmethod
    def age_must_be_positive(cls, v):
        if v is not None:
            if v <= 0:
                raise ValueError('Age must be positive')
            if v > 120:
                raise ValueError('Age cannot exceed 120')
        return v

    @field_validator('course')
    @classmethod
    def course_must_not_be_empty(cls, v):
        if v is not None:
            if not v.strip():
                raise ValueError('Course cannot be empty')
            if len(v) > 100:
                raise ValueError('Course must be less than 100 characters')
            return v.strip()
        return v


class StudentResponse(StudentBase):
    """Schema for student response"""
    id: int

    class Config:
        from_attributes = True
