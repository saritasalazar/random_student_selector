import random
from data import student_list

new_list = []

# Select a random student


def random_student():
    list_length = len(student_list)
    n = random.randint(0, list_length - 1)

# Add the student name to the new_list and print the name to the console
    new_list.append(student_list[n])
    print(student_list[n])

# Save all the student names in new_list to the file student_list.text
    with open('student_list.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % student for student in new_list)

# Ask the user if they would like to select another student
    ask_user()


def ask_user():
    user_input = input("Choose another student y/n? ").lower()
    if user_input == "y":
        print("The next student is: ")
        random_student()
    else:
        print("Exiting program.")


random_student()
