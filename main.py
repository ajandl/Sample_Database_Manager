"""
Main script for the Sample Database Manager.

Defines necessary funcitons, classes, and manages program flow as required.
"""

import sqlite3
import os
from menu_class import Menus

# Get path for current script
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_PATH)

# Set path for default DB file
DEFAULT_DB = os.path.join(SCRIPT_PATH, 'DummyDB', 'DummyDB1.db')
print(DEFAULT_DB)


def connect_db(db_file):
    """
    Creates a connection to the specified database.

    dbFile [string]: Name of database file

    return [Connection object or None]: Connection object to the database file
                                        or None if unsucessful
    """

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as err:
        print("Error {0}:".format(err.args[0]))

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
    menu_main()
