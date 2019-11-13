#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program does some calculation


def main():
    user_string = input("Enter a string: ")
    user_number = int(input("Howmany times you want to repeat the string: "))
    if user_number > 0:
        print(((user_string+"")*user_number, "{}".
              format(user_number)), "Return time is:{}".format(user_number))
    else:
        print("I dont know")


if __name__ == "__main__":
    main()
