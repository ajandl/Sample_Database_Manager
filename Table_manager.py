"""
Manages database connections, table creation and manipulation, record creation
and manipulation.
"""

import sqlite3
import os
from connection_manager import ConnectionManager

class Table_manager(object):
    

    def __init__(self):
        pass

    def connect_db(self, db_file):
        """
        Creates a connection to the specified database.

        dbFile [string]: Name of database file

        return [Connection object or None]: Connection object to the database file
                                            or None if unsucessful
        """

        try:
            self.con = sqlite3.connect(db_file)
            return self.con
        except sqlite3.Error as err:
            print("Error {0}:".format(err.args[0]))


    def create_table(self, target_db, table_title):
        """
        Creates a  table in the target database

        targetDB : Connection object to the target database

        table_title [str] : Title of the new database

        return : None
        """
        with ConnectionManager(target_db) as con:
            self.curss = con.cursor()

            target_table = ''' CREATE TABLE IF NOT EXISTS ''' + table_title + '''()'''
            self.curss.execute(target_table)
            self.con.commit()
    

    def enter_data(self, target_table):
        """
        Creates a new record in the target table

        Prompts user for input for each field in the table.

        This is an inefficient way to enter data, eventually the program should
        support importing from csv or xlsx files.

        target_table [str] : Table where record will be created

        return : None
        """
        pass