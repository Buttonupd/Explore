# import dependencies
from urllib.request import urlopen
from io import StringIO
import csv
import numpy as np


def request():

    # using python urllib request to read csv file from external file
    # load data and post it in the console
    # pass the csv url, read the file and decode it with ascii mode on
    data = urlopen('https://focusmobile-interview-materials.s3.eu-west-3.amazonaws.com/Cheap.Stocks'
                   '.Internationalization'
                   '.Currencies.csv').read().decode('ascii', 'ignore')

    # read the data variable
    datafile = StringIO(data)

    # read using csv reader variable and pass the data file
    csvReader = list(map(list, csv.reader(datafile)))

    # create a for loop
    for _ in csvReader:
        user = input('Enter a Currency: ')

        if user in np.array(csvReader)[:, 0]:
            print(user + ":\nYou have entered the name of a country. \nPlease enter a Country Currency. ")

        elif user in np.array(csvReader)[:, 1]:
            print(user + ":\nYou have entered the Country Currency instead of the code."
                         " \nIt still is a supported Currency Code in the application.")

        elif user in np.array(csvReader)[:, 2]:
            print(user + ':\nThis is a supported Currency in our application.')

        elif user == "":
            break

        else:
            print(user + ":\nConfirm whether the name and spelling of the Currency you have entered is correct."
                         "\nIf it is, then this Currency is not supported at the moment.\nBut we are all always "
                         "working around the clock to integrate more Currencies.")


request()
