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

        str_to_print = ""

        str_to_print += self.title + '\n'
        str_to_print += '-'*len(self.title) + '\n'

        for elem in range(1, len(self.options)+1):
            str_to_print += str(elem) + '. ' + self.options[elem][0] +'\n'

        return str_to_print


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
            current_options.append(elem[0])

        if option_number in self.options.keys():
            raise Exception("This option number has already been assigned. \
                             Use another number for the option.")
        elif option_title in current_options:
            raise Exception("This option title has already been used. \
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

        return self.options[selected_option][1]


    def remove_option(self, selected_option):
        """
        Remove the selected option from the options dictionary

        selected_option [int] : Key value associated with desired option

        return None
        """

        if selected_option in self.options:
            del self.options[selected_option]
        else:
            raise Exception("The option to be removed is not in this menu. \
                             Select an option between 1 and \
                             {0}".format(len(self.options)+1))
