# import dependencies

import pandas as pd
import numpy as np


def currency():
    """
    this function helps compute different features of the program
    :return:
    """
    # load the csv data
    data = pd.read_csv('Cheap.Stocks.Internationalization.Currencies.Csv')

    # convert the csv data into a 2d array
    data = data[['Country', 'Currency', 'ISO 4217 Code']]

    # use the inbuilt map function to execute a function for each item in an iterable
    listed_currencies = list(map(list, data.values))

    # initialize an empty string variable which will be used as a user input field
    user = ""

    # iterate the listed_currencies sequence
    for _ in listed_currencies:

        user = input('Enter currency: ')

        if user in np.array(listed_currencies)[:, 0]:
            print(user + ":\nYou have entered the name of a country. \nPlease enter a Country Currency. ")

        elif user in np.array(listed_currencies)[:, 1]:
            print(user + ":\nYou have entered the Country Currency instead of the code."
                         " \nIt still is a supported Currency Code in the application.")

        elif user in np.array(listed_currencies)[:, 2]:
            print(user + ':\nThis is a supported Currency in our application.')

        else:
            print(user + ":\nConfirm whether the name and spelling of the Currency you have entered is correct."
                         "\nIf it is, then this Currency is not supported at the moment.\nBut we are all always "
                         "working around the clock to integrate more Currencies.")


# call the function
currency()
