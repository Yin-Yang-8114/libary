from valdiations import user_choice
from display import display_menu

def main():
    user_choice =user_choice()
    while user_choice != 8:
        display_menu()
        if user_choice == 1:
            display_all_books()
        elif user_choice == 2:
            search_book_by_name()
        elif user_choice == 3:
            add_new_book()
        elif user_choice == 4:
            borrow_book()
        elif user_choice == 5:
            return_book()
        elif user_choice == 6:
            display_available_books()
        elif user_choice == 7:
            display_books_by_author()
        user_choice = user_choice()