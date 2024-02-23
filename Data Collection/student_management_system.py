#CRUD - Create Read Update Delete
# Student Management System
'''
1. Login as an admin
2. Login as a student

Admin Operations
- Add new student
- Update an existing student
- Delete student
- Read all students

Student Operations
- Read data of student
'''

studentsData = [
    {"s_id":101, "s_name":"John", "s_phone":9898988898},
    {"s_id":102, "s_name":"Sam", "s_phone":9898988000},
    {"s_id":103, "s_name":"Mac", "s_phone":9898988444},
    {"s_id":104, "s_name":"Nick", "s_phone":9898988874}
    ]

while True:
    print("""
    1. Login as admin
    2. Login as student
    """)
    choice = int(input("Enter your choice : "))

    if choice == 1:
        print("Login as admin")
        print("""
    1. Add new student
    2. Delete student
    3. Update student
    4. Read all students
    5. Search Student
    """)
        admin_choice = int(input("Enter your choice : "))
        if admin_choice == 1:
            s_id = int(input("Enter Student ID : "))
            s_name = input("Enter Student Name : ")
            s_phone = input("Enter Student Phone No : ")
            student = {"s_id":s_id, "s_name":s_name, "s_phone":s_phone}
            studentsData.append(student)
        elif admin_choice == 2:
            s_id = int(input("Enter Student ID you want to delete : "))
            for i in range(len(studentsData)):
                if studentsData[i]["s_id"] == s_id:
                    studentsData.pop(i)
                    break
        elif admin_choice == 3:
            pass
        elif admin_choice == 4:
            for i in range(len(studentsData)):
                print(studentsData[i])
        elif admin_choice == 5:
            pass
        else:
            print("Invalid Choice...")
    else:
        print("Login as student")











