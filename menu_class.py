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
        self.options = {}


    def __str__(self):
        """ Defines print styling for menus """
        pass


    def add_option(self, option_number, option_title, option_function):
        """
        Adds option to current menu

        Options are stored in a dictionary keyed with the option_number. The values are tuples with (option_title, option_function)
        """
        current_options = []
        for elem in self.options.values:
            current_options.append = elem[0]
            
        pass