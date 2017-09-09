"""
Main script for the Sample Database Manager.

Defines necessary funcitons, classes, and manages program flow as required.
"""

import sqlite3
import os

# Get path for current script
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_PATH)

# Set path for default DB file
DEFAULT_DB = os.path.join(SCRIPT_PATH, 'DummyDB', 'DummyDB3.db')
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


if __name__ == "__main__":
    USER_DB = input("Provide full file path for database or enter 'default': ")

    if USER_DB == 'default':
        connect_db(DEFAULT_DB)
        print("Connected to default DB: DummyDB1.db")
    else:
        connect_db(USER_DB)
        print("Connected to user specified DB at: ", USER_DB)
