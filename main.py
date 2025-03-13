import counter
import logger
from os import system
import time
import datetime


def choose():
    print("Welcome to the best counter! YOU WILL STOP FAPPING NIGGA!")
    print()
    print("choose actions")
    print("1. logger [track your progresss and write down your downs]")
    print("2. see who much days without fapping")
    print("3. RESET LIKE CLOWNS!")
    print("4. am out!~~")
    print()

    action = input("type the number and nothing else: ")

    print()

    if action == "1" or action == "2" or action == "3" or action == "4":
        return action
    else:
        print("you are an idiot!")
        time.sleep(3)
        system("clear||cls")
        choose()

def clown():
    if input("reset logs(y/n)? ") == "y":
        f = open("logs.txt", "w")
        f.write("")
        f.close
    
    if input("reset date(y/n)?") == "y":
        f = open("date.txt", "w")
        if input("old date or now?(old/now)") == "now":
            today = datetime.datetime.now().strftime('%H:%M %d-%m-%Y')
            f.write(str(today))
            f.close
        else:
            f.write(input("Well well well, type the sate in this format and \n\
                          I am not reponsible of any brick! \n\
                          format is like 04:05 15-03-2025: "))
            f.close

    print("Done!")
    time.sleep(3)
    system("clear||cls")
    runner()

def runner():
    user_input = choose()
    if user_input == "1":
        system("clear||cls")
        logger.main()
    elif user_input == "2":
        system("clear||cls")
        counter.main()
    elif user_input == "3":
        system("clear||cls")
        clown()

runner()