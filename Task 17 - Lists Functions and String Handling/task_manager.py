"""# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files."""

# =====importing libraries===========
import os
from datetime import date

# Global Constants
DATETIME_STRING_FORMAT = "%Y-%m-%d"
USER_FILE = "user.txt"
TASK_FILE = "tasks.txt"

MENU_INSTRUCT = (
    "Enter the number of the task to edit or mark as complete, "
    + "or '-1' to return to the main menu: "
)


# Utility Functions
def file_exists(file_name):
    """Check if a file exists."""
    return os.path.exists(file_name)


def write_default_admin():
    """Write a default admin user to the user file."""
    with open(USER_FILE, "w", encoding="utf8") as file:
        file.write("admin;password\n")


# Load Users
def load_users():
    """Load users from the user file into a dictionary."""
    users = {}
    if file_exists(USER_FILE):
        with open(USER_FILE, "r", encoding="utf8") as file:
            for line in file:
                username, password = line.strip().split(";")
                users[username] = password
    return users


# Save user
def save_users(users):
    """Save the updated users dictionary back to the user file."""
    with open(USER_FILE, "w", encoding="utf8") as file:
        for username, password in users.items():
            file.write(f"{username};{password}\n")


# Add tasks
def add_task():
    """Add a new task to the task file."""
    task_username = input("Enter the username of the person the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the task description: ")
    task_due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
    assigned_date = date.today().strftime(DATETIME_STRING_FORMAT)
    completed = "No"

    output = (
        f"{task_username};{task_title};{task_description};"
        + f"{task_due_date};{assigned_date};{completed}\n"
    )

    with open(TASK_FILE, "a", encoding="utf8") as file:
        file.write(output)
    print("Task added successfully.")


# Save Tasks
def save_tasks(tasks):
    """Save the updated tasks back to the task file."""
    with open(TASK_FILE, "w", encoding="utf8") as file:
        for task in tasks:
            file.write(";".join(task) + "\n")


# Show all tasks
def view_all_tasks():
    """View all tasks present in the task file."""
    if not file_exists(TASK_FILE):
        print("There are no tasks to show.")
        return

    with open(TASK_FILE, "r", encoding="utf8") as file:
        tasks = file.readlines()

    for task in tasks:
        username, title, description, due_date, assigned_date, completed = (
            task.strip().split(";")
        )
        print(
            f"Task: {title}\n"
            f"Assigned to: {username}\n"
            f"Due Date: {due_date}\n"
            f"Assigned Date: {assigned_date}\n"
            f"Completed: {completed}\n"
            f"Description: {description}\n"
        )


# View logged in user's tasks
def view_my_tasks(current_user):
    """View tasks assigned to the logged-in user."""
    if not file_exists(TASK_FILE):
        print("You have no tasks assigned.")
        return

    with open(TASK_FILE, "r", encoding="utf8") as file:
        tasks = [
            line.strip().split(";") for line in file if line.startswith(current_user)
        ]

    if not tasks:
        print("You have no tasks assigned.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. Task: {task[1]} - Due Date: {task[3]} - Completed: {task[5]}")
        selected_task = input(MENU_INSTRUCT)
        if selected_task.isdigit():
            selected_task = int(selected_task)
            if 1 <= selected_task <= len(tasks):
                task = tasks[selected_task - 1]
                action = input(
                    "Do you want to (m)ark as complete or (e)dit the task? "
                ).lower()
                if action == "m":
                    task[5] = "Yes"
                    print("Task marked as complete.")
                elif action == "e":
                    new_username = input(
                        "Enter new username (leave blank to keep current): "
                    )
                    if new_username:
                        task[0] = new_username
                    new_due_date = input(
                        "Enter new due date (YYYY-MM-DD, "
                        + "leave blank to keep current): "
                    )
                    if new_due_date:
                        task[3] = new_due_date
                    print("Task updated.")
                else:
                    print("Invalid action.")
            else:
                print("Invalid task number.")
        elif selected_task == "-1":
            return
        else:
            print("Invalid input.")
        # Save the updated tasks
        save_tasks(tasks)


# Register User
def register_user(users):
    """Register a new user by adding them to the users dictionary and file."""
    new_username = input("Enter new username: ")
    if new_username in users:
        print("This username already exists. Please try a different username.\n")
        return
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")
    if new_password == confirm_password:
        users[new_username] = new_password
        print("New user successfully added.")
        save_users(users)
    else:
        print("Passwords do not match. User not added.")


# Main Function
def main():
    """Main function to run the application."""
    if not file_exists(USER_FILE):
        write_default_admin()

    users = load_users()

    current_user = None
    while current_user is None:
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print("Login successful.\n")
            current_user = username
        else:
            print("Invalid login. Please try again.\n")

    while True:
        print(
            "\nSelect an option: \n"
            "   r   -  Register user \n"
            "   a   -  Add task \n"
            "   va  -  View all tasks \n"
            "   vm  -  View my tasks \n"
            "   e   -  Exit \n"
        )
        choice = input("Enter choice: ").lower()

        if choice == "r" and current_user == "admin":
            register_user(users)
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all_tasks()
        elif choice == "vm":
            view_my_tasks(current_user)
        elif choice == "e":
            break
        else:
            print("Invalid option, please try again.\n")


if __name__ == "__main__":
    main()
