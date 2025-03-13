import datetime
from os import system
import time
import ranks

def main():
    # read files
    saved_date = open("date.txt", "r")
    logs = open("logs.txt", "r")

    # setup dates
    previous_date = datetime.datetime.strptime(saved_date.read(), '%H:%M %d-%m-%Y')
        
    while True:
        today = datetime.datetime.now()

        # compute difference
        left_time = (today - previous_date)#.seconds
        
        # print output
        print("starting date: ", previous_date)
        print("time left:     ", left_time)
        
        print()

        ndays = left_time.days
        print("numbers of days: ",ndays )


        ranks.rank(ndays)

        print()

        print("Logs of downs:")
        for x in logs:
            print(x)

            
        #reset screen
        time.sleep(60)
        system("clear||cls")