import datetime
from os import system
import time

def main():
    print("Welcome to counter logger!")

    # prepare vars
    today = datetime.datetime.now()
    logs = open("logs.txt", "r")

    print()

    # print logs
    print("logs:")
    for x in logs:
        print(x)

    print()

    user_input = input("type q to exit or reason of your down: ")
    if user_input == "q":
        return 0
    else:
        # enter edit mode
        f = open("logs.txt", "a")
        f.write("[" + str(today) + "] " + user_input + "\n")
        f.close()
        print("saved!")
        time.sleep(3)
        system("clear||cls")
        main()