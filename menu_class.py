"""
Defines menu class for sample database manager
"""

class Menus(object):
    """
    Defines menu class for sample database manager

    Modified print functionality provided by __str__

    add_option allows for adding new options to menu

    execute allows for running the user selected option
    """

    def __init__(self, menu_title):
        self.title = menu_title
        self.options = []


    def __str__(self):
        """ Defines print styling for menus """
        pass


    def add_option(self, option_name):
        """
        Adds option to current menu

        Need to decide how to store option name, corresponding option fucntion, and option number
        """
        pass
