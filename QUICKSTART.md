# ⚡ Quick Start Guide

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 2️⃣ Run the Application

```bash
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

## 3️⃣ Open Interactive API Docs

Open your browser and go to: **http://localhost:8000/docs**

You'll see the Swagger UI where you can test all endpoints interactively!

## 4️⃣ Try a Quick Test

### Create a Student (POST)
Click on **POST /create-student/** and enter:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 20,
  "course": "Computer Science"
}
```

Click **Execute** → You'll get back the created student with an ID!

### Get All Students (GET)
Click on **GET /students-all/** and click **Execute**

You'll see all students in the database.

### Get Single Student (GET)
Click on **GET /student/{id}** and enter the ID from the created student.

### Update Student (PUT)
Click on **PUT /update-students/{id}** and modify any fields:

```json
{
  "age": 21,
  "course": "Data Science"
}
```

### Delete Student (DELETE)
Click on **DELETE /delete-students/{id}** to remove a student.

## 5️⃣ Test with Python Script

```bash
python test_examples.py
```

This will automatically test all endpoints with sample data!

## 📊 Project Files Overview

| File | Purpose |
|------|---------|
| `main.py` | FastAPI application with all endpoints |
| `database.py` | Database setup & configuration |
| `models.py` | Student database model |
| `schemas.py` | Pydantic validation schemas |
| `requirements.txt` | Python dependencies |
| `test_examples.py` | Automated API tests |

## 🔗 Useful Links

- **API Docs (Swagger)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc
- **Root Endpoint**: http://localhost:8000/

## ⚙️ Common Commands

```bash
# Run with hot reload (development)
python main.py

# Stop the server
Press CTRL+C

# Run tests
python test_examples.py

# Check database
ls -la *.db
```

## 🆘 Issues?

### API won't start?
- Make sure port 8000 is not in use
- Check if all dependencies are installed

### Can't connect?
- Ensure the server is running
- Check if you're using the correct URL (http://localhost:8000)

### Database errors?
- Delete `students.db` and restart the app
- The database will be recreated automatically

---

**You're all set! Start exploring the API! 🚀**
