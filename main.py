"""
Main script for the Sample Database Manager.

Defines necessary funcitons, classes, and manages program flow as required.
"""

import sqlite3
import os
from menu_class import Menus
from connection_manager import ConnectionManager

# Get path for current script
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
# print(SCRIPT_PATH)

# Set path for default DB file
DEFAULT_DB = os.path.join(SCRIPT_PATH, 'DummyDB', 'DummyDB1.db')
# print(DEFAULT_DB)


def print_data(target_table, print_length):
    """
    Prints the header and the top print_length records of the target table

    target_table [str] : Table with desired data

    print_length [int] : Max number of records to print

    return : None
    """
    pass


def rtn_to_menu(target_menu):
    """
    Prints target menu and prompts for user input

    target_menu [Menus] : Menus object of target menu

    return : None
    """
    pass


""" Old main_menu """
# def menu_main():
#     """
#     Displays main menu and allows selection from it.

#     No parameters or return
#     """

#     print("\nMain menu:")
#     print("-------------\n")
#     print("1. Create table in database")
#     print("2. Enter data into table")
#     print("3. Get data from table")
#     choice = input("Enter number of selection: ")

main_menu = Menus("Main Menu")
main_menu.add_option(1, "Create new table", create_table)
main_menu.add_option(2, "Enter data to table", enter_data)
main_menu.add_option(3, "Get data from table", print_data)
main_menu.add_option(9, "Exit", exit)



def main():
    """
    Executes main function

    No parameters.
    """

    user_db = input("Provide full file path for database or enter 'default': ")

    if user_db == 'default':
        connect_db(DEFAULT_DB)
        print("Connected to default DB: DummyDB1.db")
    else:
        connect_db(user_db)
        print("Connected to user specified DB at: ", user_db)


if __name__ == "__main__":
    main()
    print(main_menu)
    main_menu.get_option(int(input("Enter index of menu selection: ")))()
