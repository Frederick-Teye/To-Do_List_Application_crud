import sqlite3
import os
from datetime import date

db_path = "to-do_list.db"


def main():
    if not os.path.exists(db_path):
        conn = None
        try:
            # create connection to db_file
            conn = sqlite3.connect(db_path)

            # create cursor object
            cur = conn.cursor()

            # sql statement to create To-do_list table
            sql = """CREATE TABLE To-do_list (To-do_ID INTEGER PRIMARY KEY NOT NULL, 
                                              Description TEXT NOT NULL,
                                              DueDate TEXT NOT NULL,
                                              DaysLeftOrOverdue INTEGER NOT NULL,
                                              Priority TEXT NOT NULL,
                                              PriorityNumber INTEGER NOT NULL,
                                              Status TEXT NOT NULL,
                                              StatusNumber INTEGER NOT NULL)"""

            # create To-do_list table
            cur.execute(sql)

            # commit changes
            conn.commit()
        except sqlite3.Error as err:
            # print error message generated by sql
            print(err)
        finally:
            # close connection if there was any
            if conn is not None:
                conn.close()
    else:
        # if the database file already exists, then update all the status and status number column
        update_status()
        menu()


""" 
The main function creates to-do_list.db, which is the database for the program if none
exists. After creating the database, it creates the the table that will
be used in this program. The table's name is To-do_list. If the database
already exists, then the main function will go ahead and update the 
status for all the rows in the table by calling the update_status 
function and then call the menu function. THIS IS MY LAST DOCSTRING.
"""


def update_status():
    conn = None
    try:
        conn = sqlite3.connect(db_path)

        cur = conn.cursor()

        # read only To-do_ID and DueDate from each row in database for
        cur.execute("SELECT To-do_ID, DueDate, Status FROM To-do_list")

        # save the data in a variable
        results = cur.fetchall()

        # create a variable to hold updated values
        update = []

        if len(results) > 0:
            for row in results:
                days_remaining = date.fromisoformat(row[1]) - date.today()

                # save the outcome string into a list by splitting at where there are spaces
                days_remaining_list = days_remaining.__str__().split(" ")

                # we want only the number of days overdue or remaining
                days_remaining = int(days_remaining_list[0])

                # if the status of the data is not completed or overdue
                # then update the status, while you updated days remaining too.
                # Put all these updates and To-do_ID into the update list
                if row[2] != "Completed" or row[2] != "Overdue":
                    if days_remaining < 0:
                        abs_days_remaining = abs(days_remaining)
                        update.append((abs_days_remaining, "Overdue", 3, row[0]))
                    elif days_remaining == 0:
                        update.append((days_remaining, "In progress", 2, row[0]))
                    else:
                        update.append((days_remaining, "Pending", 1, row[0]))
                elif row[2] == "Completed":
                    abs_days_remaining = abs(days_remaining)
                    update.append((abs_days_remaining, "Completed", 4, row[0]))
                else:
                    abs_days_remaining = abs(days_remaining)
                    update.append((abs_days_remaining, "Overdue", 4, row[0]))

            # update all the rows in the database.
            for row in update:
                cur.execute("""UPDATE To-do_list
                               SET DaysLeftOrOverdue = ?,
                               SET Status = ?,
                               SET StatusNumber = ?
                               WHERE To-do_ID == ?""",
                            row)

            # commit all changes
            conn.commit()
    except sqlite3.Error as err:
        # print error message generated by sql
        print(err)
    except ValueError:
        print("The program tried to process wrong value.")
    finally:
        # close connection if there was any
        if conn is not None:
            conn.close()


def menu():
    count = 0
    if count == 0:
        print("        To-Do List Menu       \n"
              "------------------------------")
        option = input("1. Add new to-do item to list\n"
                       "2. View all to-do items in list\n"
                       "3. View a specific to-do item\n"
                       "4. Edit/Update a to-do item\n"
                       "5. Delete to-do item(s) in list\n"
                       "6. Exit application\n"
                       "Enter your choice: ")
        count += 1
    else:
        print("\n        To-Do List Menu       \n"
              "------------------------------")
        option = input("1. Add new to-do item to list\n"
                       "2. View all to-do items in list\n"
                       "3. View a specific to-do item\n"
                       "4. Edit/Update a to-do item\n"
                       "5. Delete to-do item(s) in list\n"
                       "6. Exit application\n"
                       "Enter your choice: ")
        # I won't add 1 to count again, because at this point I have achieved what I want to achieve
        # with the count variable, which is to add space before the second menu

    if option == "1":
        add_new_item()
    elif option == "2":
        view_items()
    elif option == "3":
        view_an_item()
    elif option == "4":
        update_a_list_item()
    elif option == "5":
        delete_item()
    elif option == "6":
        exit_application()
    else:
        print("\nInvalid input..."
              "\nPlease enter either 1, 2, 3, 4, 5 or 6")
        menu()


def item_status(days_left):
    days = int(days_left)
    if days < 0:
        return "Overdue"
    elif days == 0:
        return "In progress"
    else:
        return "Pending"


def days_lft(due_date):
    days_in_sentence = due_date - date.today()
    days = days_in_sentence.split(" ")
    return abs(int(days[0]))


def item_status_number(status):
    if status == "Pending":
        return 1
    elif status == "In progress":
        return 2
    else:
        return 3


def add_new_item():
    description = input("Enter a short description for this to-do item: ")
    due_date = get_due_date()  # this function gets t date from the user and return value

    days_left = days_lft(due_date)  # this function returns the number of days left

    status = item_status(days_left)  # return status of the item description

    status_number = item_status_number(status)  # returns the status number

    priority = ""
    priority_number = ""

    priority_dict = {"1": ["High", 1], "2": ["Medium", 2], "3": ["Low", 3]}

    priority_selection = input("1. Critical / High\n"
                               "2. Normal / Medium\n"
                               "3. Optional / Low\n"
                               "Enter your choice: ")

    while True:
        if priority_selection in priority_dict:
            priority = priority_dict[priority_selection[0]]
            priority_number = priority_dict[priority_selection[1]]
            break
        else:
            print("Invalid input...\n"
                  "Enter either 1, 2, or 3")
            priority_selection = input("1. Critical / High\n"
                                       "2. Normal / Medium\n"
                                       "3. Optional / Low\n"
                                       "Enter your choice: ")

    conn = None
    try:
        conn = sqlite3.connect()
        cur = conn.cursor()

        sql = """INSERT INTO To-do_list (Description, DueDate, DaysLeftOrDue,
                                         Priority, PriorityNumber, Status, StatusNumber)
                                  VALUES(?, ?, ?, ?, ?, ?, ?)"""

        cur.execute(sql, (description, due_date, days_left, priority,
                          priority_number, status, status_number))

        # commit data added
        conn.commit()
    except sqlite3.Error as err:
        print(err)
    finally:
        # close connection
        if conn is not None:
            conn.close()

# define all the functions used in add_new_item()
# the operations that this functions perform will be needed in other functions,
# that is why I have put those operations inside a function so that they can
# be called whenever needed.


def get_due_date():
    print("\nAt this point, you will be asked to enter day, month, then year...")

    # get day
    day = input("\nEnter day: ").strip()
    while True:
        if day.isnumeric():
            break
        else:
            print("\nYou can only enter numbers")
            day = input("Enter day: ").strip()

    month = get_month()

    while True:
        year = input("Enter year: ")
        if len(year) == 4 and year.isnumeric() and int(year) >= date.today().year:
            return f"{year}-{month}-{day.zfill(2)}"
            # .zfill(2) is to pad the day with a zero if it is only a single digit
        else:
            print(f"You can't enter a year below {date.today().year} or non-numeric characters\n")


def get_month():
    months = {
        "1": "01", "Jan": "01",
        "2": "02", "Feb": "02",
        "3": "03", "Mar": "03",
        "4": "04", "Apr": "04",
        "5": "05", "May": "05",
        "6": "06", "Jun": "06",
        "7": "07", "Jul": "07",
        "8": "08", "Aug": "08",
        "9": "09", "Sep": "09",
        "10": "10", "Oct": "10",
        "11": "11", "Nov": "11",
        "12": "12", "Dec": "12"
    }

    while True:
        user_input = input("\nYou can enter the number or the three-letter abbreviation for the month \n"
                           "(e.g., '1' or 'Jan', '3' or 'Mar' or '11' or 'Nov'):").strip().capitalize()

        if user_input in months and int(user_input):
            return months[user_input]
        else:
            print("Invalid input... Please enter a valid month or its number.")







