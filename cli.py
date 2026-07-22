import os
import platform


from seed import seed_database
from models.config import recreate_db

from helpers import(
    exit_program,
    list_departments,
    find_department_by_name,
    find_department_by_id,
    create_department,
    update_department,
    delete_department,
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_department_employees,
)

def clear_screen():
    """Clears the console screen"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def pause():
    input("\nPress Enter to return to menu...")

def menu():
    print("-------Department---------")
    print("1. List all departments")
    print("2. Find department by name")
    print("3. Find department by id")
    print("4. Create department")
    print("5. Update department")
    print("6. Delete department")
    print("--- Employee-------")
    print("7. List all employees")
    print("8. Find employee by name")
    print("9. Find employee by id")
    print("10. Create employee")
    print("11. Update employee")
    print("12. Delete employee")
    print("13. List all employees in a department")

def main():
    try:
        recreate_db()
        seed_database()
        print("Database initialized successfully")
    except Exception as exc:
        print(f"Error setting up the database: {exc}")
    while True:
        clear_screen()
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_departments()
            pause()
        elif choice == "2":
            find_department_by_name()
            pause()
        elif choice == "3":
            find_department_by_id()
            pause()
        elif choice == "4":
            create_department()
            pause()
        elif choice == "5":
            update_department()
            pause()
        elif choice == "6":
            delete_department()
            pause()
        elif choice == "7":
            list_employees()
            pause()
        elif choice == "8":
            find_employee_by_name()
            pause()
        elif choice == "9":
            find_employee_by_id()
            pause()
        elif choice == "10":
            create_employee()
            pause()
        elif choice == "11":
            update_employee()
            pause()
        elif choice == "12":
            delete_employee()
            pause()
        elif choice == "13":
            list_department_employees()
            pause()

if __name__ == "__main__":
    main()
