# import required modules
import sys
import time
import datetime

# function to show usage of our program
def usage():
    print("countdown.py <number>")

# countdown timer function
def countdown_timer():
    # countdown = int(input("Enter time here"))
    # check if user passed in any CMD arguments
    if len(sys.argv) == 2:
        # check if argument can be converted to an interger
        try:
            countdown = int(sys.argv[1])
        except ValueError:
            # throw an error because argument is not an interger convertible
            print("Please enter a valid number")
            sys.exit(-1)
    else:
        # show if no arguments passed or if more that required passed
        usage()
        sys.exit(-1)
    
    # create an infinite loop
    while countdown > 0:
        # 00:00:00
        # create time and convert it to string using time delta function
        countdown_time = str(datetime.timedelta(seconds=countdown))
        
        # print time
        print(countdown_time)
        time.sleep(1)
        countdown -= 1
    print("countdown finished")

# create main function
def main():
    countdown_timer()

# invoke main function
if __name__ == '__main__':
    main()
