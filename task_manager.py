# ************ Compulsory Task 1 and 2 ************

''' This program assists a small business to manage tasks assigned to 
each member of the team. The adminstrator is the only one who has 
permission to register new users and view the statistics of how many 
users are registered, as well as number of tasks. '''

# Define a function to allow only users registered to log in.
def authenticate(user_name, password):
    ''' Open and read the file where all registered team members' 
    usernames and passwords are stored. '''
    with open('user.txt', 'r') as file:
        # Separate username and password on each line.
        for line in file:
            stored_username, stored_password = line.strip().split(", ")
            ''' Check if the entered user name and password 
            match as on the registered users. '''
            if user_name == stored_username and password == stored_password:
                return True
    return False

# Request user to enter their username and password.
user_name = input("Please enter your user name: ")
password = input("Please enter your password: ")

''' Use the authenticate function to check if username and 
password are on the registered user list file. '''
while not authenticate(user_name, password):
    print("\nIncorrect username or password. Please try again.")
    user_name = input("Please enter your user name: ")
    password = input("Please enter your password: ")

print("\n\033[1mYou have successfully logged in.\033[0m\n")

# Define the menu users can select an option to continue with.
while True:
    #  Convert user input to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - display number of users and tasks
e - exit
: ''').lower()

# This option of the menu registers new user.
    if menu == 'r':
        ''' The permission to registere a new user is 
        only reserved for the admnistrator.'''
        if user_name == "admin":
            # Request admin to enter username and password of new user.
            new_user_name = input("Please eneter user name to be registered: ")
            password = input("Please eneter new user's password: ")
            # Request admin to confirm password.
            password_confirmation = input("Please enter password again: ")
            # Check if new password and confirmed password match.
            while password != password_confirmation:
                # Let admin know passwords don't match.
                print("\nPassword not confrimed, please try again.")
                # Request passwords to be entered again
                password = input("Please eneter new user's password: ")
                password_confirmation = input("Please enter password again: ")
            # If passwords match, register new user.
            if password == password_confirmation:
                new_user = f"\n{new_user_name}, {password}"
            with open('user.txt', 'a') as file:
                file.write(new_user)
                print("\n\033[1mNew user successfully registered.\033[0m\n")
        else:
            print("\nUser has no permission to register new users.\n")
        pass

# This option of the menu allows a user to add a new task.
    elif menu == 'a':
        ''' Request the user to enter the username of the person whom 
        the task is assigned to, the title of the task, the description 
        of the task, the due date of the task, the date the task was 
        assigned and indicate if the task has been completed. '''
        username = input("Enter username of the person a task is assigned: ")
        title = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task (DD MMM YYYY): ")
        current_date = input("Enter the current date (DD MMM YYYY): ")
        task_completed = input("Is the task completed? (Yes/No): ")
        task_data = f"\n{username}, {title}, {description}, {due_date}, {current_date}, {task_completed}"
        with open('tasks.txt', 'a') as file:
            file.write(task_data)
            print("\n\033[1mTask successfully added.\033[0m\n")
        pass

# This option of the menu displays all registered tasks.
    elif menu == 'va':
        print("\n\033[1mTasks for all users.\033[0m")
        with open('tasks.txt', 'r') as file:
            # Read a line, split that line where there is comma and space.
            for line in file:
                username, title, description, due_date, current_date, task_completed = line.strip().split(", ")
                print("_" * 140)
                # Display all the details of each task.
                print("\nTask: \t\t\t", title)
                print("Assigned to: \t\t", username)
                print("Date assigned: \t\t", current_date)
                print("Due date: \t\t", due_date)
                print("Task complete? \t\t", task_completed)
                print("Task description \t", description)
                print("_" * 140)
        pass

# This option of the menu displays tasks assigned to the logged in user.
    elif menu == 'vm':
        print("\n\033[1mTasks for the current user.\033[0m")
        with open('tasks.txt', 'r') as file:
            # Read a line, split that line where there is comma and space.
            for line in file:
                username, title, description, due_date, current_date, task_completed = line.strip().split(", ")
                # Give condition to consider tasks of logged in user.
                if username == user_name:
                    # Display details tasks assigned to logged in user.
                    print("_" * 140)
                    print("\nTask: \t\t\t", title)
                    print("Assigned to: \t\t", username)
                    print("Date assigned: \t\t", current_date)
                    print("Due date: \t\t", due_date)
                    print("Task Complete? \t\t", task_completed)
                    print("Task description \t", description)
                    print("_" * 140)
        pass

# Allows administrator to display total number of tasks and users.
    elif menu == 's':
        ''' The permission to display total number of tasks and users 
        is only reserved for the admnistrator.'''
        if user_name == "admin":
            with open('tasks.txt', 'r') as file:
                # Read and return each line as a string in a list.
                tasks = file.readlines()
                # Length of the string corresponding to number of tasks.
                num_tasks = len(tasks)
            with open('user.txt', 'r') as file:
                # Read and return each line as a string in a list.
                users = file.readlines()
                # Length of the string corresponding to number of users.
                num_users = len(users)
            # Dispay number of tasks and users
            print(f"\n\033[1mThe total number of tasks: {num_tasks}\033[0m")
            print(f"\n\033[1mThe total number of users: {num_users}\033[0m\n")
        else:
            print("\nUser has no permission to view statistics.\n")
        pass

# This option of the menu shuts down the program.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

# This option of the menu let user know they entered and invald option.
    else:
        print("You have entered an invalid input. Please try again")
