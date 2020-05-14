"""
Please use help() function to view the docstrings if any confusion arises
in this code. And also read the comments to clear any doubts.
"""

#importing modules starts here
import sys , time
import os
import datetime


def storing_data_file():
    """
    This function stores the data into the file.
    """
    cls()
    myfile = open("FerryData.txt", "w")
    myfile.write("*****************************************************************\n")
    myfile.write("     Ferry ID: {}               Date: {}    \n".format(choose_ferry_ID.ferry_id, todays_date))
    myfile.write("*****************************************************************\n")
    myfile.write("*    Trip Time: {}                                            *\n".format(time_departure))
    myfile.write("*****************************************************************\n")
    myfile.write("BUSINESS CLASS".center(60, " "))
    myfile.write("\n")
    myfile.write("*        {} *       {}  *        {}  *         {}  *       {}   *\n".format(business_class[0][0],business_class[0][1],business_class[0][2],business_class[0][3],business_class[0][4]) )

    myfile.write("*        {} *       {}  *        {}  *         {}  *       {}   *\n".format(business_class[1][0],business_class[1][1],business_class[1][2],business_class[1][3],business_class[1][4]) )
    myfile.write("*****************************************************************\n")
    myfile.write("ECONOMY CLASS".center(60, " "))
    myfile.write("\n")
    myfile.write("*****************************************************************\n")
    myfile.write("*        {} *       {}  *        {}  *         {}  *       {}   *\n".format(economy_class[0][0],economy_class[0][1],economy_class[0][2],economy_class[0][3],economy_class[0][4]) )
    myfile.write("*        {} *       {}  *        {}  *         {}  *       {}   *\n".format(economy_class[1][0],economy_class[1][1],economy_class[1][2],economy_class[1][3],economy_class[1][4]) )
    myfile.write("*        {} *       {}  *        {}  *         {}  *       {}   *\n".format(economy_class[2][0],economy_class[2][1],economy_class[2][2],economy_class[2][3],economy_class[2][4]) )
    myfile.write("*        {} *       {}  *        {}  *         {}  *       {}   *\n".format(economy_class[3][0],economy_class[3][1],economy_class[3][2],economy_class[3][3],economy_class[3][4]) )
    myfile.write("*        {} *       {}  *        {}  *         {}  *       {}   *\n".format(economy_class[4][0],economy_class[4][1],economy_class[4][2],economy_class[4][3],economy_class[4][4]) )
    myfile.write("*        {} *       {}  *        {}  *         {}  *       {}   *\n".format(economy_class[5][0],economy_class[5][1],economy_class[5][2],economy_class[5][3],economy_class[5][4]) )
    myfile.write("*****************************************************************\n")
    myfile.write("*     Name: {}                Contact No.:{}      *".format(name, number))

    myfile.close()
    print("Data is storing in file......")
    time.sleep(5)
    cls()
    next_seat()

#Defining functions is started
def seat_arrangement():
    ferry_file = open("FerryData.txt", "r")
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    print(ferry_file.readline())
    time.sleep(3)
    ferry_file.close()
    print("Press M to redirect to Main Menu: ")
    choose = input("")
    if choose == "M" or choose == "m":
        cls()
        main_menu()
    else:
        cls()
        main_menu()



def main_menu():
    """
    This function is called every time when user wants to go to the main menu.
    This is the initial page of the system.
    It displays three choices for user

    """
    print("_"*60)
    print("Welcome To FERRY TICKETING SYSTEM".center(60,"_"), flush = True )
    print("_"*60)
    print("\n\n\n")

    print("\n","#"*60)
    print("\n" , "P - Purchase Ticket           ".ljust(60,"="))
    print("\n",  "V - View Seating Arrangement  ".ljust(60,"="))
    print("\n",  "Q - Quit System               ".ljust(60,"="))
    print("\n", "#"*60 , "\n")
    time.sleep(0.5)
    choice = input("Enter Your Choice: ")
    if choice == "P" or choice == "p":
        #goes to the purchase menu.
        time.sleep(0.5)
        costumer_details()

    elif choice == "V" or choice == "v":
        cls()
        time.sleep(0.5)
        seat_arrangement()
    elif choice == "Q" or choice == "q":
        system_quit()
    else:
        cls()
        print("Invalid entry".center(10, "!"))
        time.sleep(0.5)
        main_menu()


def cls():
    """
    This function is called when user wants to clear the console window
    """
    os.system('cls')


def purchase_menu():
    """
    This is a purchase module. This is a sub menu.
    It displays 3 choices. B for Business Class. E for Economy class tickets.
    """
    cls()
    print("_"*60)
    print(" Welcome to Purchase Module ".center(60, "_"))
    print("_"*60)

    print("\n\n\n","#"*60)
    print("\n" ,"B - Business Class ".ljust(60, "="))
    print("\n" ,"E - Economy Class  ".ljust(60, "="))
    print("\n" ,"M - Main Menu      ".ljust(60, "="), "\n")

    choice1 = input("Enter Your choice: ")
    if choice1 == "B" or choice1 == "b":
        cls()
        time.sleep(0.5)
        business_class_booking()

    elif choice1 == "E" or choice1 == "e":
        cls()
        time.sleep(0.5)
        economy_class_booking()

    elif choice1 == "M" or choice1 == "m":
        cls()
        print("\n\n\n\n\n")
        print("  You are being redirected to Main Men.... ".center(60, " "))
        time.sleep(0.5)
        cls()
        main_menu()
    else:
        cls()
        print("Sorry!!! Invalid Input", "\nPlease Enter Valid entry")
        time.sleep(0.5)
        purchase_menu()


def choose_ferry_ID():
        """
        It lets user to select Ferry Id.
        There are 8 Ferrys.

        """
        cls()
        print("#"*60)
        print("Select your desired Ferry ID".center(60, " "))
        print("#"*60)
        print("\n\n")
        print("1. 001-Penang-Langkawi")
        print("2. 002-Penang-Langkawi")
        print("3. 003-Penang-Langkawi")
        print("4. 004-Penang-Langkawi")
        print("5. 005-Langkawi-Penang")
        print("6. 006-Langkawi-Penang")
        print("7. 007-Langkawi-Penang")
        print("8. 008-Langkawi-Penang")
        print("\n")
        try:
            choice_ID = int(input("Enter Your Choice: "))
        except ValueError:
            print("Please enter Correct credentials..")
            print("You are being redirected to choosing ferry ID....")
            time.sleep(3)
            choose_ferry_ID()
        else:
            if choice_ID == 1:
                choose_ferry_ID.ferry_id = "001-Penang-Langkawi"                    #User chooses any ferry Id from this function.
                trip_timing_penang_langkawi()                                                       #after choosing the ferry id user is redirected to trip timing.
            elif choice_ID == 2:
                choose_ferry_ID.ferry_id = "002-Penang-Langkawi"
                trip_timing_penang_langkawi()
            elif choice_ID == 3:
                choose_ferry_ID.ferry_id = "003-Penang-Langkawi"
                trip_timing_penang_langkawi()
            elif choice_ID == 4:
                choose_ferry_ID.ferry_id = "004-Penang-Langkawi"
                trip_timing_penang_langkawi()
            elif choice_ID == 5:
                choose_ferry_ID.ferry_id = "005-Langkawi-Penang"
                trip_timing_langkawi_penang()
            elif choice_ID == 6:
                choose_ferry_ID.ferry_id = "006-Langkawi-Penang"
                trip_timing_langkawi_penang()
            elif choice_ID == 7:
                choose_ferry_ID.ferry_id = "007-Langkawi-Penang"
                trip_timing_langkawi_penang()
            elif choice_ID == 8:
                choose_ferry_ID.ferry_id = "008-Langkawi-Penang"
                trip_timing_langkawi_penang()

            else:
                print("Invalid Entry.")
                time.sleep(0.5)
                choose_ferry_ID()


def trip_timing_penang_langkawi():

    global time_departure
    cls()
    time.sleep(0.5)
    print("#"*60)
    print("Select Your preferred timing of Trip".center(60, " "))
    print("#"*60)

    print("\n\n\n")
    print("1. 10AM Penang To Langkawi")
    print("2. 11AM Penang To Langkawi")
    print("3. 12PM Penang To Langkawi")
    print("4. 1PM  Penang To Langkawi")
    print("\n\n")
    choice_time = int(input("Enter your timing: "))
    if choice_time == 1:
        time_departure = "10AM"
        purchase_menu()

    elif choice_time == 2:
        time_departure = "11AM"
        purchase_menu()

    elif choice_time == 3:
        time_departure = "12PM"
        purchase_menu()
    elif choice_time == 4:
        time_departure = "1PM"
        purchase_menu()
    else:
        cls()
        print("Invalid Entry".center(70, "!"), "\nPlease Enter".center(70, " "))
        trip_timing_penang_langkawi()


def costumer_details():
    """
    This function take details of customer
    """
    global name
    global number
    print("\n\n\n")
    print("Please Enter traveller's details".center(80," "))

    name = input("Enter Name of traveller:  ")
    number = input("ENter Traveller's Contact Number: ")
    time.sleep(2)
    choose_ferry_ID()


def trip_timing_langkawi_penang():
        """
        This function is used for selecting the time of trip for langkawi to penang.
        """
        global time_departure                                                   #this function is called if user choose a feery id for langkawi to penang.
        cls()
        time.sleep(0.5)
        print("#"*60)
        print("Select Your preferred timing of Trip".center(60, " "))
        print("#"*60)

        print("\n\n\n")
        print("1. 2PM  Langkawi To Penang")
        print("2. 3PM  Langkawi To Penang")
        print("3. 4PM  Langkawi To Penang")
        print("4. 5PM  Langkawi To Penang")
        print("\n\n")
        choice_time = int(input("Enter your timing: "))
        if choice_time == 1:
            time_departure = "2PM"
            purchase_menu()

        elif choice_time == 2:
            time_departure = "3PM"
            purchase_menu()

        elif choice_time == 3:
            time_departure = "4PM"
            purchase_menu()
        elif choice_time == 4:
            time_departure = "5PM"
            purchase_menu()
        else:
            cls()
            print("Invalid Entry".center(70, "!"), "\nPlease Enter".center(70, " "))
            trip_timing_langkawi_penang()



def next_seat():
    """
    This function asks user for next booking of seat in the same ferry.
    """
    print("Do you like to book next seat?")
    print("\n")
    next_booking = input("Enter Y to book next seat and N for Quitting system: ")
    if next_booking == "Y" or next_booking == "y":
        cls()
        purchase_menu()
    elif next_booking == "n" or next_booking == "N":
        main_menu()
    else:
        print(" Invalid Entry ".center(60, "!"))
        next_seat()



def system_quit():
    """
    This Function quits the system by displaying some messages.
    """
    cls()
    print("\n\n\n\n")
    print("Your system is closing.!!!".center(80, " "))
    print("Have a Good Day".center(80, " "))
    time.sleep(2)
    exit()


def business_class_booking():
    """
    This function takes row and column of seat for business class.
    Given that rows are 1 and 0. And columns are 0, 1, 2, 3, 4.
    """
    print("\n\n")
    print("Business Class has total 10 seats which is arranged in 2 rows and 5 columns.")
    print("Here, 0 means first row and 1 means second.")
    print("Similarly, in columns 0 means first 1 means second and so on....  upto 4 which means fifth column.")
    print("\n\n\n")
    time.sleep(4)
    booked = False
    while booked != True:
        try:
            row = int(input("Enter row of the seat from either 0 or 1: "))
            column = int(input("Enter column of the seat: "))
        except IndexError:      #if input is greater than the index range of seat then IndexError is handled.
            cls()
            print("\n\n\n\n")
            print("Please Enter correct credentials")
            print("Your are being redirected to choose seat number......")
            time.sleep(3)
            business_class_booking()        #redirects to the same function to redo the method.

        else:
            if business_class[row][column] == 1:
                print("*"*60)
                print("Seat is already booked".center(60, " "))
                print("Please Choose next seat".center(60, " "))
            else:
                print("Seat Is available")
                print("Booking your seat.....")
                time.sleep(3)
                business_class[row][column] = 1
                cls()
                print("\n\n" , "  Your Seat is booked Now  ".center(60, " "),"\n\n")
                print("  Enjoy Your Ride  ".center(60, " "))
                booked = True
                time.sleep(1)
                storing_data_file()


def economy_class_booking():
    """
    This function asks user for the seat number of economy class.
    """
    print("\n\n")
    print("Economy Class has total 40 seats which is arranged in 2 rows and 5 columns.")
    print("Here, 0 means first row ,1 means second and so on upto 7 which means eighth row.")
    print("Similarly, in columns 0 means first 1 means second and so on....  upto 4 which means fifth column.")
    print("\n\n\n")
    time.sleep(4)

    booked = False
    while booked != True:
        row = int(input("Enter row of the seat: "))
        if row not in range(5):
            print("Please enter between 0 to 4 ")
            economy_class_booking()
        column = int(input("Enter column of the seat in range 0 to 4: "))

        if economy_class[row][column] == 1:
            print("*"*60)
            print("Seat is already booked".center(60, " "))
            print("Please Choose next seat".center(60, " "))
        else:
            print("Seat Is available")
            print("Booking your seat.....")
            time.sleep(2)
            economy_class[row][column] = 1
            print("\n\n","Your Seat is booked Now", "\n\n")
            print("         Enjoy Your Ride     ")
            booked = True
            time.sleep(0.5)
            storing_data_file()


todays_date = datetime.date.today()

business_class = []
business_class.append([0,0,0,0,0])
business_class.append([0,0,0,0,0])

economy_class = []
economy_class.append([0,0,0,0,0])
economy_class.append([0,0,0,0,0])
economy_class.append([0,0,0,0,0])
economy_class.append([0,0,0,0,0])
economy_class.append([0,0,0,0,0])
economy_class.append([0,0,0,0,0])
economy_class.append([0,0,0,0,0])
economy_class.append([0,0,0,0,0])

main_menu()




