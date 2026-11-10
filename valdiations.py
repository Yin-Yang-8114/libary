def user_choice():
    while True:
        display_menu()
        choice = input("Enter your choice (1-11): ")
        if choice.isdigit() and 1 <= int(choice) <= 11:
            return int(choice)
        else:
            print("invalid choice. please enter a number between 1 and 8.")