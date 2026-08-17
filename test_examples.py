"""
Test examples for Student Management System API
Run the main.py first, then you can use this script to test the API
"""

import requests
import json

BASE_URL = "http://localhost:8000"

# ANSI color codes for better output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text:^60}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}\n")


def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")


def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.END}")


def print_info(text):
    print(f"{Colors.CYAN}ℹ {text}{Colors.END}")


def print_request(method, endpoint, data=None):
    print(f"{Colors.BLUE}{method} {endpoint}{Colors.END}")
    if data:
        print(f"{Colors.YELLOW}Request Body:{Colors.END}")
        print(json.dumps(data, indent=2))


def print_response(response):
    print(f"{Colors.YELLOW}Response Status:{Colors.END} {response.status_code}")
    try:
        print(f"{Colors.YELLOW}Response Body:{Colors.END}")
        print(json.dumps(response.json(), indent=2))
    except:
        print(response.text)


def test_health_check():
    print_header("1. HEALTH CHECK")
    print_request("GET", f"{BASE_URL}/health/")
    
    response = requests.get(f"{BASE_URL}/health/")
    print_response(response)
    
    if response.status_code == 200:
        print_success("API is running!")
    else:
        print_error("API is not responding correctly")


def test_create_student():
    print_header("2. CREATE STUDENT")
    
    students_data = [
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": 20,
            "course": "Computer Science"
        },
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "age": 22,
            "course": "Data Science"
        },
        {
            "name": "Bob Johnson",
            "email": "bob.johnson@example.com",
            "age": 21,
            "course": "Software Engineering"
        }
    ]
    
    created_students = []
    
    for student_data in students_data:
        print_info(f"Creating student: {student_data['name']}")
        print_request("POST", f"{BASE_URL}/create-student/", student_data)
        
        response = requests.post(
            f"{BASE_URL}/create-student/",
            json=student_data
        )
        print_response(response)
        
        if response.status_code == 201:
            print_success(f"Student created successfully!")
            created_students.append(response.json())
        else:
            print_error(f"Failed to create student")
        print()
    
    return created_students


def test_get_all_students():
    print_header("3. GET ALL STUDENTS")
    print_request("GET", f"{BASE_URL}/students-all/")
    
    response = requests.get(f"{BASE_URL}/students-all/")
    print_response(response)
    
    if response.status_code == 200:
        students = response.json()
        print_success(f"Retrieved {len(students)} student(s)")
    else:
        print_error("Failed to retrieve students")


def test_get_single_student(student_id):
    print_header(f"4. GET SINGLE STUDENT (ID: {student_id})")
    print_request("GET", f"{BASE_URL}/student/{student_id}")
    
    response = requests.get(f"{BASE_URL}/student/{student_id}")
    print_response(response)
    
    if response.status_code == 200:
        print_success("Student retrieved successfully!")
    else:
        print_error("Failed to retrieve student")


def test_update_student(student_id):
    print_header(f"5. UPDATE STUDENT (ID: {student_id})")
    
    update_data = {
        "name": "John Doe Updated",
        "age": 21,
        "course": "Artificial Intelligence"
    }
    
    print_request("PUT", f"{BASE_URL}/update-students/{student_id}", update_data)
    
    response = requests.put(
        f"{BASE_URL}/update-students/{student_id}",
        json=update_data
    )
    print_response(response)
    
    if response.status_code == 200:
        print_success("Student updated successfully!")
    else:
        print_error("Failed to update student")


def test_delete_student(student_id):
    print_header(f"6. DELETE STUDENT (ID: {student_id})")
    print_request("DELETE", f"{BASE_URL}/delete-students/{student_id}")
    
    response = requests.delete(f"{BASE_URL}/delete-students/{student_id}")
    print_response(response)
    
    if response.status_code == 204:
        print_success("Student deleted successfully!")
    else:
        print_error("Failed to delete student")


def test_validation_errors():
    print_header("7. VALIDATION TESTS")
    
    # Test 1: Invalid email
    print_info("Test 1: Invalid email format")
    invalid_email = {
        "name": "Test User",
        "email": "invalid-email",
        "age": 20,
        "course": "Test Course"
    }
    print_request("POST", f"{BASE_URL}/create-student/", invalid_email)
    response = requests.post(f"{BASE_URL}/create-student/", json=invalid_email)
    print_response(response)
    print()
    
    # Test 2: Negative age
    print_info("Test 2: Negative age")
    negative_age = {
        "name": "Test User",
        "email": "test@example.com",
        "age": -5,
        "course": "Test Course"
    }
    print_request("POST", f"{BASE_URL}/create-student/", negative_age)
    response = requests.post(f"{BASE_URL}/create-student/", json=negative_age)
    print_response(response)
    print()
    
    # Test 3: Empty name
    print_info("Test 3: Empty name")
    empty_name = {
        "name": "",
        "email": "test2@example.com",
        "age": 20,
        "course": "Test Course"
    }
    print_request("POST", f"{BASE_URL}/create-student/", empty_name)
    response = requests.post(f"{BASE_URL}/create-student/", json=empty_name)
    print_response(response)


def run_all_tests():
    print(f"\n{Colors.BOLD}{Colors.HEADER}")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║   STUDENT MANAGEMENT SYSTEM API - TEST SUITE               ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print(f"{Colors.END}\n")
    
    try:
        # Run tests in sequence
        test_health_check()
        created_students = test_create_student()
        test_get_all_students()
        
        if created_students:
            first_student_id = created_students[0]['id']
            test_get_single_student(first_student_id)
            test_update_student(first_student_id)
        
        test_validation_errors()
        
        if created_students:
            # Delete the first student as a final test
            test_delete_student(first_student_id)
        
        # Print summary
        print_header("TEST SUITE COMPLETED")
        print_success("All tests have been executed!")
        print_info("Check the responses above for any errors")
        
    except requests.exceptions.ConnectionError:
        print_error("\n✗ Could not connect to the API")
        print_info("Make sure the FastAPI server is running:")
        print_info("  python main.py")
    except Exception as e:
        print_error(f"\n✗ An error occurred: {str(e)}")


if __name__ == "__main__":
    run_all_tests()
