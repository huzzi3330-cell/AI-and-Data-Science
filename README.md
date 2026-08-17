# Student Management System API

A fast and efficient REST API for managing student records built with FastAPI and SQLAlchemy.

## 📋 Features

- ✅ **Create** new students with validation
- ✅ **Read** all students or a specific student by ID
- ✅ **Update** student information
- ✅ **Delete** students
- ✅ Email uniqueness validation
- ✅ Input validation with Pydantic
- ✅ SQLite database integration
- ✅ Automatic API documentation (Swagger UI + ReDoc)
- ✅ Error handling with proper HTTP status codes
- ✅ Database session management

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Python**: 3.7+

## 📦 Installation

### 1. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Start the Server

```bash
python main.py
```

Or use uvicorn directly:

```bash
uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

### Access Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📚 API Endpoints

### 1. Create Student
```
POST /create-student/
```
**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 20,
  "course": "Computer Science"
}
```
**Response:** 201 Created
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "age": 20,
  "course": "Computer Science"
}
```

### 2. Get All Students
```
GET /students-all/?skip=0&limit=100
```
**Response:** 200 OK
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 20,
    "course": "Computer Science"
  }
]
```

### 3. Get Single Student
```
GET /student/{id}
```
**Response:** 200 OK
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "age": 20,
  "course": "Computer Science"
}
```

### 4. Update Student
```
PUT /update-students/{id}
```
**Request Body (all fields optional):**
```json
{
  "name": "Jane Doe",
  "age": 21,
  "course": "Data Science"
}
```
**Response:** 200 OK

### 5. Delete Student
```
DELETE /delete-students/{id}
```
**Response:** 204 No Content

### 6. Health Check
```
GET /health/
```
**Response:** 200 OK
```json
{
  "status": "OK",
  "message": "Student Management API is running"
}
```

## ✅ Validation Rules

| Field | Rules |
|-------|-------|
| **name** | Required, max 100 characters, cannot be empty |
| **email** | Required, valid email format, must be unique |
| **age** | Required, must be positive (1-120), cannot exceed 120 |
| **course** | Required, max 100 characters, cannot be empty |

## 📁 Project Structure

```
project/
├── main.py           # FastAPI application with all endpoints
├── database.py       # SQLAlchemy database configuration
├── models.py         # Database models (Student)
├── schemas.py        # Pydantic schemas for validation
├── requirements.txt  # Project dependencies
└── students.db       # SQLite database (auto-created)
```

## 🧪 Testing with cURL

### Create a Student
```bash
curl -X POST "http://localhost:8000/create-student/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "age": 20,
    "course": "Computer Science"
  }'
```

### Get All Students
```bash
curl "http://localhost:8000/students-all/"
```

### Get Single Student
```bash
curl "http://localhost:8000/student/1"
```

### Update Student
```bash
curl -X PUT "http://localhost:8000/update-students/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Doe",
    "age": 21
  }'
```

### Delete Student
```bash
curl -X DELETE "http://localhost:8000/delete-students/1"
```

## 🔧 Configuration

### Database URL
The database URL is configured in `database.py`:
```python
DATABASE_URL = "sqlite:///./students.db"
```

To use a different database (e.g., PostgreSQL):
```python
DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use a different port
uvicorn main:app --reload --port 8001
```

### SQLite Database Locked
- Close any other connections to the database
- Delete `students.db` and restart the application

### Module Not Found Errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

## 📝 Error Responses

### 400 Bad Request
```json
{
  "detail": "Email 'john@example.com' already registered"
}
```

### 404 Not Found
```json
{
  "detail": "Student with ID 999 not found"
}
```

### 422 Unprocessable Entity (Validation Error)
```json
{
  "detail": [
    {
      "loc": ["body", "age"],
      "msg": "Age must be positive",
      "type": "value_error"
    }
  ]
}
```

## 📖 Learning Outcomes

This project demonstrates:
- ✅ FastAPI framework fundamentals
- ✅ RESTful API design principles
- ✅ SQLAlchemy ORM usage
- ✅ Database relationships and constraints
- ✅ Pydantic data validation
- ✅ Error handling and HTTP status codes
- ✅ Dependency injection in FastAPI
- ✅ CRUD operations

## 📄 License

This project is open source and available under the MIT License.

---

**Happy coding! 🚀**
