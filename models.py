from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):
    """Student database model"""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    course = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}', age={self.age}, course='{self.course}')>"
