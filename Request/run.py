#! /usr/bin/env python3.7

# define a function to compute the code below


def main():
    print("Welcome to Help Menu. Choose one or more")

    # use while loop function to execute a code for different conditions
    while True:
        """
            in this code I have defined a while loop code which checks for different conditions
            A menu for the user to guide them through running the program.
            """

        print("Help Menu: \nhelp - View help menu "
              "\nrn - run the program \nex - exit the program")

        short_code = input().lower()
        if short_code == 'help':

            print("-" * 10)
            print("In the terminal, type python run.py. This the name of the executable file. \n"
                  "You are prompted to key in a currency value. \n"
                  "For example, Kenya's Currency is Kenyan shilling. \n"
                  "Replace with a value of your own.")
            print('To go back to the menu,click the ENTER key on your Keyboard')

        elif short_code == 'rn':
            # execute the main code if this code is called
            from request import request
            request()
            print("-" * 10)

        elif short_code == "ex":
            print("Bye ...")
            print("-" * 10)
            break

        else:
            print("Invalid command")
            print("-" * 10)


if __name__ == '__main__':
    main()
