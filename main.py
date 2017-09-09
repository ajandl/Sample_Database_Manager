"""
Main script for the Sample Database Manager.

Defines necessary funcitons, classes, and manages program flow as required.
"""

import sys
import os
import sqlite3

def connect_db(db_file):
    """
    Creates a connection to the specified database.

    dbFile: Name of database file

    return: Connection object to the database file or None if unsucessful
    """

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as err:
        print("Error {0}:".format(err.args[0]))

