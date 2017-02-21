import getpass
from validators import check_pass
from messages import *


def user_chooser(user_choice):
    switcher = {'1': loggin, '2': registration, , '3': helpp, '4': exit}
    return switcher[user_choice]()


@check_pass()
def loggin():

    
    username = input('Enter username: ')
    password = getpass.getpass('Enter your password: ')


def registration():
    username = input('Enter username: ')
    password = getpass.getpass('Enter your password: ')
    re_password = getpass.getpass('Retype password: ')


def helpp():
    pass


def exit():
    sys.exit()


def main_menu():
    print(WELCOME_USER_MESSAGE)
    user_choice = input()
    user_chooser(user_choice)


def main():
    main_menu()

if __name__ == '__main__':
    main()
