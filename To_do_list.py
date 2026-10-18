import os
while True:
    print("Welcome to the To-Do List")
    user_note = input("Do you want to add a new To-Do item?: ")

    if user_note == "yes":
        user_note = input("add your To-Do List: ")


    if user_note == "exit":
        print("Thank you for using the to-do list.")
        break