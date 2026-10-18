import os
while True:
    print("Welcome to the To-Do List")
    user_note = input("Do you want to add a new To-Do item? (y/n, or exit): ")

    if user_note == "y":
        item = input("add your To-Do List: ")
        with open("to_do.text", "a", encoding="utf-8") as file:
            file.write(item +"\n")


    if user_note == "exit":
        print("Thank you for using the to-do list.")
        break

    elif user_note == "n":
        show = input("Do you want to list your To-Do items? (y/n): ")
        if show == "y":
            if os.path.exists("to_do.txt"):
                with open("to_do.text", "r", encoding="utf-8") as file:
                    for line in file:
                        print(line.strip())
            else:
                print("Your list is empty.")