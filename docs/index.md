Beau Barth 

11/19/2019

IT FDN 100 A Au 19: Foundations Of Programming: Python

Week 7 - Assignment 01: Error Handling and Pickling

# To Do List - Error Handling and Pickling

_**Author's Note:**_

_This week I again decided to approach this document more akin to a high level design or application design document. Data outline and examples are presented in a similar format._

_I also chose to expand on my existing To Do List script from last week and implement error handling for input of file name during read/write._

_Unfortunately, I consistently ran into issues with my code for pickle.load method, and was unsuccessful in finding any path to resolution through internet search, review of the lecture or discussion board. The error handling ironically seems to however do its job when encountered during the management of binary files._

## Scope/Requirements:

This script must satisfy the following requirements:

- The program must provide a method for the user to read an indicated .txt file and load each existing task and its priority into a list, with each task/priority existing as an independent dictionary within the list
- The program must provide a method for the user to read an indicated .dat file and load each existing task and its priority into a list, with each task/priority existing as an independent dictionary within the list
- The program must provide a method for the user to view the current list of tasks
- The program must provide a method for the user to add additional task(s) and their priority to the current list
- The program must provide a method for the user to remove existing tasks from the current list
- The program must provide a method for the user to write the current list to an indicated .txt file 
- The program must provide a method for the user to write the current list to an indicated .dat file 
- The program must provide a method for the user to exit the program

## Classes

This script will introduce two classes:

- **FileProcessor** - A class which includes functions for reading and writing the to-do list data to and from text file
- **IO** - A class which includes functions for add, remove and display of task data, as well as capturing user operation choice

## Functions
This script introduces the following  functions. For clarity, functions are organized below by class.

### FileProcessor.ReadFileDataToList()
- **Purpose:** Read data from text file, append each row as new dictionary in data list
- **Params:** file_name (string); list_of_rows (list)
- **Return:** list_of_rows (list)

### FileProcessor.ReadBinaryFileDataToList()
- **Purpose:** Read data from binary file, append each row as new dictionary in data list
- **Params:** file_name (string); list_of_rows (list)
- **Return:** list_of_rows (list)

### FileProcessor.WriteListDataToFile()
- **Purpose:** Write data from current list of tasks into text file
- **Params:** file_name (string); list_of_rows (list)
- **Return:** nothing

### FileProcessor.WriteListDataToBinaryFile()
- **Purpose:** Write data from current list of tasks into binary file
- **Params:** file_name (string); list_of_rows (list)
- **Return:** nothing

### IO.OutPutMenuItems()
- **Purpose:** Display a menu of choices to the user
- **Params:** none
- **Return:** nothing

### IO.InputMenuChoice()
- **Purpose:** Gets the menu choice from the user
- **Params:** none
- **Return:** choice (string)

### IO.ShowCurrentItemsInList()
- **Purpose:** Shows the current tasks in the data table
- **Params:** list_of_rows (list)
- **Return:** nothing

### IO.AddNewItemInList()
- **Purpose:** Add New Task to current data list
- **Params:** task (string); priority (string); list_of_rows (list)
- **Return:** list_of_rows (list)

### IO.RemoveItemFromList()
- **Purpose:** Removes a task from the data table based on user input
- **Params:** task (string); list_of_rows (list)
- **Return:** list_of_rows (list)


## Order of Operations
The following text describes the order of operations, and various logical steps required to execute each operation within this script.

1.	Upon initilization, `IO.OutPutMenuItems()` is called to display a menu of operations and prompt user for input. `IO.InputMenuChoice()` is then called to determine the user input/operation selection.

_Fig 01 – Operations for displaying operations menu to user, and determining user choice_
 
2.	For the Load Task List from File operation, the user is first prompted to identify the desired file type, and identify the file name. If the file is not found, an error is returned to the user. When loading data from a text file, a `for` loop is utilized to iterate over the data in the text file and output to the task list. When loading data from a binary file the same loop is used, preceded by `pickle.load()` . In either case, once complete, these tasks and their priority are subsequently displayed to the user via a `print()` method.

_Fig 02 – Operation for Loading Task List from File (Text or Binary)_

_Fig 03 – Example of try/except error handling for indicated file name in Load Task List from File operation_

3.	For the Review Current Tasks operation, the function `IO.ShowCurrentItemsInList()` is called.  A `for` loop is utilized to iterate over the current list of tasks in the `lstTable` list. These tasks and their priority are subsequently displayed to the user via a `print()` method.

4.	For the Add New Task operation, `input()` methods are utilized to capture new values for task and priority from the user. The function `IO.AddNewItemInList()` is then called, and these values are assigned within a new dictionary, and appended to the existing data in `lstTable` list. `IO.ShowCurrentItemsInList()` is called once more to display to the user the updated `lstTable` list.

5.	For the Remove Existing Task operation, an `input()` method is used to capture the task to be removed from the user. The function `IO.RemoveItemFromList()` is then called. This function uses a `for` loop to iterate over the current list, and an `if` statement to filter the list for the task indicated. If found, the task (the impacted dictionary itself) is then removed from the list. Following a confirmation of task removal printed to the user, the function `IO.ShowCurrentItemsInList()` is called once more to display to the user the updated `lstTable` list.

_Fig 04 – Operations for Reviewing, Adding to, and Removing from Task List_

6.	For the Save Task Data to Text File operation, the function `IO.ShowCurrentItemsInList()` is called first to display to the user the current tasks in `lstTable` list.  The user is then prompted to identify the `.txt` file they intend to save to. An `input()` method is used to capture confirmation of save from the user. If user confirms intent to save, the function `FileProcessor.WriteListDataToFile()` is called. This function utilizes a `for` loop to iterate over the current `lstTable` list, and utilizes the `write()`  method to author each task and its priority to the indicated text file. I utilized the function open() and mode "W"  so that the updated list of tasks would overwrite the current list in the text file. 

_Fig 05 – Operation for saving Task List to Text File_

7.	For the Save Task Data to Binary File operation, the function `IO.ShowCurrentItemsInList()` is called first to display to the user the current tasks in `lstTable` list.  The user is then prompted to identify the `.dat` file they intend to save to. An `input()` method is used to capture confirmation of save from the user. If user confirms intent to save, the function `FileProcessor.WriteListDataToFile()` is called. This function utilizes a `for` loop to iterate over the current `lstTable` list, creates a list of this data, and uses the `pickle.dump` method to store to the `.dat` file, which has been opened in `"wb+"` mode to allow for writing in bytes, and support error handling.

_Fig 06 - Operation for saving Task List to Binary File_

8.	For the Exit the program operation, I used a `break` statement to end the `while` loop, and subsequently end the script.

_Fig 08 – Operation for exiting the program_

## Validation
Prior to executing my script for testing I used https://pythonbuddy.com/,  an online python validator, to verify any warnings or errors in my script. Usually this site works for me, but for some reason it was not functioning properly, as if it would not read my code.

I then executed the script in both PyCharm and Command Prompt. While i was able to verify my conditions for loading from text file, viewing task list, adding/removing tasks, saving to text or binary file and exiting the program all worked, i was unable to successfully pass testing of my operation for loading to task list from a binary file type.

Below i have included screenshots specifically for validation of loading/saving to and from text and binary files, and the errors (and error handling!) encountered.

 
_Fig 09 – Executing Assignment07 in PyCharm- Operation 1 - Testing error handling for bad file name_

_Fig 10 – Executing Assignment07 in PyCharm- Operation 1 - Testing success for load tasks from indicated Text File_

_Fig 11 – Executing Assignment07 in PyCharm- Operation 1 - Error Encountered when attempting load from Binary File_

_Fig 12 – Executing Assignment07 in PyCharm- Operation 5 - Saving to text file_

_Fig 13 – Executing Assignment07 in PyCharm- Operation 6 - Saving to binary file_

_Fig 14 – Executing Assignment07 in Command Prompt - Operation 1 - Testing error handling for bad file name_

_Fig 15 – Executing Assignment07 in Command Prompt - Operation 1 - Testing success for load tasks from indicated Text File_

_Fig 16 – Executing Assignment07 in Command Prompt - Operation 1 - Error Encountered when attempting load from Binary File_

_Fig 17 – Executing Assignment07 in Command Prompt - Operation 5 - Saving to text file_

_Fig 18 – Executing Assignment07 in Command Prompt - Operation 6 - Saving to binary file_

## Summary
In retrospect, I probably could have elected to author a new script, from scratch, but I wanted to challenge myself to continue building on last week's assignment which I also felt gave me an opprotunity to "put it all together" with respect to file read/write, pickling, and error handling. A new, simpler script probably would have made for an easier time in troubleshooting however.

Unfortunately, I could not seem to find success with `pickle.load`. This made it further difficult for me to verify whether the lists I saved to a binary file via Operation 6 were saved in the format intended. The text file looks correct, but I would prefer to be certain.

Appreciate any suggestion or feedback you as the reader are able to provide on the error encountered in my `FileProcessor.ReadBinaryFileDataToList()` function, where the error is encountered.

### References used this week:
https://pythonprogramming.net/python-pickle-module-save-objects-serialization

https://www.pythoncentral.io/how-to-pickle-unpickle-tutorial/

https://docs.python.org/3/library/exceptions.html

https://docs.python.org/3/library/pickle.html

