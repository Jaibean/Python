#
# Python 3.9
#
#Author: Jaimie Bertoli
#
# Purpose: The Tech Academy - Python Course, Drill 4 of 63 Demonstrating how to
# pass in the variable. return variable means we are returning the variable to
# the calling function
#







def start():
    print("Hello {}!".format(get_name()))

def get_name():
    name = input("What is your name? ") 
    return name





if __name__ == " __main__":
    start()
