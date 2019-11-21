# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Error Handling and Pickling
# # ChangeLog (Who,When,What):
# Beau Barth,11.18.2019, Created Script
# Beau Barth,11.19.2019, Updated Script
# Beau Barth,11.20.2019, Updated Script
# ------------------------------------------------------------------------ #

import pickle  # import pickle methods

# Declare variables and constants
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection


class FileProcessor:  # includes functions for reading and writing the to-do list data to and from text file

    @staticmethod
    def ReadFileDataToList(file_name, list_of_rows):
        """
        Desc - Reads data from a text file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) of tasks in data table, populated by rows in file
        :return (list) of tasks in data table
        """
        try:
            file = open(file_name, "r+")
            for line in file:
                data = line.split(",")
                row = {"task": data[0].strip(), "priority": data[1].strip()}
                list_of_rows.append(row)
            file.close()
            return list_of_rows
        except FileNotFoundError as e:  # file not found error handling
            print("Unable to locate the indicated file name!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:  # generic error handling
            print("There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def ReadBinaryFileDataToList(file_name, list_of_rows):
        """
        Desc - Reads data from a binary file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) of tasks in data table, populated by rows in file
        :return (list) of tasks in data table
        """
        try:
            with open(file_name, 'rb+') as file:
                datatounpack = pickle.load(file)
                for line in datatounpack:
                    data = line.split(",")
                    row = {"task": data[0].strip(), "priority": data[1].strip()}
                    list_of_rows.append(row)
                file.close()
            return list_of_rows
        except FileNotFoundError as e:  # file not found error handling
            print("Unable to locate the indicated file name!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:  # generic error handling
            print("There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def WriteListDataToBinaryFile(file_name, list_of_rows):
        """
        Desc - Writes data from a list of dictionary rows into a BINARY file using ab+

        :param list_of_rows: (list) containing dictionary rows:
        :param file_name: (string) with name of file:
        :return nothing
        """
        rowstodump = []
        with open(file_name, 'wb+') as file:
            for row in list_of_rows:  # use for loop to append each row found in table list to indicated binary file
                rowstodump += (row["task"] + "," + row["priority"] + "\n")
            pickle.dump(rowstodump, file)  # use pickle.dump to dump binary data to indicated file
            file.close()

    @staticmethod
    def WriteListDataToTextFile(file_name, list_of_rows):
        """
        Desc - Writes data from a list of dictionary rows into a TEXT file using a+

        :param list_of_rows: (list) containing dictionary rows:
        :param file_name: (string) with name of file:
        :return nothing
        """
        file = open(file_name, "w+")
        for row in list_of_rows:  # use for loop to append each row found in table list to indicated text file
            file.write(row["task"] + "," + row["priority"] + "\n")
        file.close()


class IO:  # includes functions for add, remove and display of task data, as well as capturing user operation choice

    @staticmethod
    def OutputMenuItems():
        """
        Desc - Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Load Task List from file
        2) Review Current Tasks
        3) Add New Task
        4) Remove Existing Task.
        5) Save Task Data to Text File
        6) Save Task Data to Binary File
        7) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """
        Desc - Gets the menu choice from a user

        :return: (string) user choice
        """
        choice = str(input("Which option would you like to perform? [1 to 7] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """
        Desc - Shows the current tasks in the data table

        :param list_of_rows: (list) of tasks in data table you want to display
        :return: nothing
        """
        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row["task"] + " (" + row["priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def AddNewItemInList(task, priority, list_of_rows):
        """
        Desc - Adds new task to current data table

        :param list_of_rows: (list) of tasks in data table to which new task will be appended
        :return: (list) of tasks in data table, including new task
        """
        try:
            dicrow = {"task": task, "priority": priority}  # assign task, priority values to new dictionary
            list_of_rows.append(dicrow)  # append new dictionary to list
            print("Task added successfully...\n")  # confirm addition
            return list_of_rows
        except:
            print("Could not add task successfully! Something is missing. Please try again.")

    @staticmethod
    def RemoveItemFromList(task, list_of_rows):
        """
        Desc - Removes a task from the data table based on user input

        :param task: (string) identifying the queried task/item:
        :param list_of_rows: (list) containing dictionary rows:
        :return: list of rows in data table, updated following task removal
        """
        try:
            for item in list_of_rows:  # iterate over current list. for each item,
                if item["task"] == task:  # if value of task is equivalent to user input
                    list_of_rows.remove(item)  # remove the item dictionary from list
                    print("Task successfully removed...")  # confirm removal
            return list_of_rows
        except:
            print("Could not remove task! Unable to locate. Please try again.")


# Display a menu of choices to the user
while True:
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Run ReadFileDataToList or ReadBinaryFileDataToList function if "Load Task List" operation selected
    if strChoice.strip() == '1':
        print("Warning: This will replace all unsaved changes. Data loss may occur!")  # Warn user of data loss
        strYesOrNo = input("Reload file data without saving? [y/n] - ")  # Double-check with user
        if strYesOrNo.lower() == 'y':
            dataChoice = input("Which file type? [binary/text]: ")  # Confirm file type
            if dataChoice.lower() == 'binary':
                fileName = input("Identify the .dat file you wish to load data from: ")
                FileProcessor.ReadBinaryFileDataToList(fileName, lstTable)  # read binary file data
                IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
            if dataChoice.lower() == 'text':
                fileName = input("Identify the .txt file you wish to load data from: ")
                FileProcessor.ReadFileDataToList(fileName, lstTable)  # read text file data
                IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        else:
            input("File data was NOT loaded! Press the [Enter] key to return to menu.")
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Run ShowCurrentItemsInList function if "Review Current Tasks" operation selected
    if strChoice.strip() == '2':
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Run AddNewItemInList function if "Add New Task" operation selected
    elif strChoice.strip() == '3':
        strTask = str(input("What is the task? ")).strip()  # Get task from user
        strPriority = str(input("What is the priority? [high|low] ")).strip()  # Get priority from user
        IO.AddNewItemInList(strTask, strPriority, lstTable)  # Add task to Data table
        print()  # Add an extra line for looks
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Run RemoveItemInList function if "Remove Existing Task" operation selected
    elif strChoice == '4':
        item_name = str(input("Enter a task to remove: ")).strip()  # Get task from user
        IO.RemoveItemFromList(item_name, lstTable)  # Remove task from Data table
        print()  # Add an extra line for looks
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Run WriteListDataToFile function if "Save Task Data to Text File" operation selected
    elif strChoice == '5':
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        fileName = input("Identify the .txt file you wish to save your current task list to: ")
        if "y" == str(input("Saving your changes to this file will overwrite existing data. Save this data to file? ("
                            "y/n) - ")).strip().lower():  # Double-check with user
            FileProcessor.WriteListDataToTextFile(fileName, lstTable)  # Save task data table to text file
            input("Data saved to file! Press the [Enter] key to return to menu.")  # Confirm file save
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Run WriteListDataToBinaryFile function if "Save Task Data to Binary File" operation selected
    elif strChoice == '6':
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        fileName = input("Identify the .dat file you wish to save your current task list to: ")
        if "y" == str(input("Saving your changes to this file will overwrite existing data. Save this data to file? ("
                            "y/n) - ")).strip().lower():  # Double-check with user
            FileProcessor.WriteListDataToBinaryFile(fileName, lstTable)  # Save task data table to binary file
            input("Data saved to file! Press the [Enter] key to return to menu.")  # Confirm file save
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Break While Loop if "Exit Program" operation selected
    elif strChoice == '7':
        break  # and Exit

