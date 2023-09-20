import time
import random

items = []
total_time = 30

# This is causes a delay after a message is pronted for easy reading


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

# This function gives the user the option to restart a concluded game or not


def replay():
    replay_option = input("Want to play again? Y/N: ")
    replay_option = replay_option.lower()
    if replay_option == 'y':
        start()
    elif replay_option == 'n':
        return False
    else:
        print("Invalid Input")
        replay()

# This function determines whether or not the bus would wait if the student
# was out of time


def bus_wait():
    b_w = random.choice(["yes", "no"])
    if b_w == "yes":
        print("Lucky you! You won't be late.")
    else:
        print("Sorry, no luck! You are LATE!!! Be up earlier next time")


def eggs_ready():
    print("preparing...")
    time.sleep(2)
    print("Your eggs are ready!")

# An option to use hot water when bathing


def hot_water():
    global total_time
    x = input("Want hot water anyway? Y/N: ")
    hotwater = x.lower()
    if hotwater == 'y':
        print_pause("Ok")
        total_time -= 15
    elif hotwater == 'n':
        print_pause("Good choice to save time")
        total_time -= 10
    else:
        print("Invalid input, please select Y or N")
        return hot_water()

# Determining what the student eats


def breakfast_options():
    global total_time
    b_o = input("1. Eggs\n"
                "2. A Sandwich\n"
                "Both made with love: ")
    if b_o == "1":
        print_pause("A quick option")
        print_pause("Just 5 minutes to prepare")
        eggs_ready()
        total_time -= 5
    elif b_o == "2":
        sandwich()
    else:
        print("Invalid input, please select 1 or 2")
        return breakfast_options()

# One of the breakfast choices wuth an option to switch


def sandwich():
    global total_time
    print_pause("Hmm...a sandwich would take about 10 minutes to prepare")
    s = input("Still want it? Y/N: ")
    s = s.lower()
    if s == 'y':
        print_pause("Ok, but if you are late, that's on you")
        print("preparing...")
        time.sleep(3)
        print('Your sandwich is ready!')
        total_time -= 10
    elif s == 'n':
        print_pause("Eggs it is!")
        eggs_ready()
        total_time -= 5
    else:
        print("Invalid input, please select Y or N")
        return sandwich()


def welcome_message():
    print_pause("You have school in 30 minutes")
    print_pause("Are you going to make it in time?")
    print_pause("You are still in bed, finish before time is up")


def get_extra_sleep():
    global total_time
    e_s = input("10 more minutes of shuteye? Y/N ")
    extra_sleep = e_s.lower()
    if extra_sleep == "y":
        print("...zzzz")
        total_time -= 10
        items.append("sleepmore")
    elif extra_sleep == "n":
        print("Good Choice")
        items.append("sleepmore")
    else:
        print("Invalid entry")
        return get_extra_sleep()


def sleep_more():
    global total_time
    print_pause("You are in the bedroom staring at the lovely, well-laid bed")
    if "sleepmore" in items:
        print_pause("Not much time left for sleep this morning")
    else:
        get_extra_sleep()


def take_a_bath_and_dress_up():
    global total_time
    if "bathed_and_dressed" in items:
        print_pause("You've had your bath and are all dressed up silly."
                    " Go do something else")
    else:
        print_pause("Time to take a bath")
        print_pause("I don't think there's time for hot water,"
                    " it will take an additional time of 5 minutes")
        hot_water()
        print("You're freshly cleaned and now dressed up!")
        items.append("bathed_and_dressed")


def eat_breakfast():
    global total_time
    print_pause("You are at the dining table")
    if "eaten" in items:
        print_pause("Hey, You! You've had breakfast already")
    else:
        print_pause("What would you like to have for breakfast?")
        breakfast_options()
        total_time -= 5
        items.append("eaten")


def play():
    global total_time
    print_pause("What would you like to do now?: ")
    task = input("1. Sleep some more\n"
                 "2. Take a bath and get dressed\n"
                 "3. Have breakfast\n")
    if task == '1':
        sleep_more()
    elif task == '2':
        take_a_bath_and_dress_up()
    elif task == '3':
        eat_breakfast()


def start():
    welcome_message()
# short-forms ar to adhere to pycodestyle
    s = "sleepmore"
    b = "bathed_and_dressed"
    e = "eaten"
    t_t = total_time
    while (s not in items or b not in items or e not in items) and t_t > 0:
        play()


start()


# Check the time after the game ends
time.sleep(1)
print("Checking the time")
time.sleep(1)
if total_time <= 0:
    print_pause("Out of time! I wonder if the bus waited for you. Let's see")
    print_pause("Checking...")
    bus_wait()
else:
    print_pause("Right on time! Get on the bus")

replay()
