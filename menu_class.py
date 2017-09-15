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

        Options are stored in a dictionary keyed with the option_number.
        The values are tuples with (option_title, option_function)

        option_number [int] : Integer assigned for the option, also used as a \
                              key in the options dict.

        option_title [str] : Description of menu option, i.e. Open Database

        option_function [function] : function or method associated with this \
                                     option.

        return None
        """
        current_options = []
        for elem in self.options.values():
            current_options.append = elem[0]

        if option_number in self.options.keys():
            raise Exception("This option number has already been assigned. \
                             Use another number for the option.")
        elif option_title in current_options:
            raise Exception("This option title has alreayd been used. \
                             Use another option title.")
        else:
            self.options[option_number] = (option_title, option_function)

        return None


    def get_option(self, selected_option):
        """
        Returns function associated with the selected option

        selected_option [int] : Key value associated with desired option

        return [function] : Returns function or method of the selected option
        """
        option_tuple = self.options[selected_option]
        return option_tuple[1] 
