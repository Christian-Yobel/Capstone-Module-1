from tabulate import tabulate # type: ignore

# Dictionary as main data container
header = ['Code', 'Project', 'Difficulty', 'Duration', 'Learning', 'Tools', 'Status', 'Date']
allProject = {
    '1001': ['Todo List', 'Beginner', '30', 'Fundamental', 'Fundamental', 'Done', '2024-01-29'], 
    '1002': ['File Organizer', 'Intermediate', '120', 'os Module', 'os Module', 'On Going', '2024-01-19'], 
    '1003': ['News Scraper', 'Advanced', '180', 'Web Scraping', 'BeautifulSoup', 'Planning', '2024-02-15'], 
    '1004': ['CSV Analyzer', 'Beginner', '45', 'File Handling', 'Pandas', 'Done', '2024-02-01'], 
    '1005': ['Data Visualizer', 'Intermediate', '90', 'Data Analysis', 'NumPy + Pandas', 'On Going', '2024-02-10'], 
    '1006': ['Spam Classifier', 'Advanced', '150', 'Machine Learning', 'Scikit-learn', 'Planning', '2024-03-01'], 
    '1007': ['Notepad App', 'Intermediate', '100', 'GUI Development', 'PyQt', 'On Going', '2024-02-20']
 }

# Dictionary as secondary data container
myProject = {
    '1001': ['Todo List', 'Beginner', '30', 'Fundamental', 'Fundamental', 'Done', '2024-01-29'], 
    '1002': ['File Organizer', 'Intermediate', '120', 'os Module', 'os Module', 'On Going', '2024-01-19']
}

# Main Program Directory
def directory():
    return input('''
Program Directory:
                 
1. Display Python Projects
2. Add New Python Projects
3. Update Python Projects
4. Delete Python Projects
5. Project Description
6. Project Guide
7. Project Basic Python Code on The Web
8. Exit

Enter Program Directory: ''')


# Confirming User Intention to go to the Main Directory from inside program 1-7
def returnChecker():
    while True:
        user = input('Go back to Main Directory? (Y/N)\nInput : ')
        if user.upper() == 'Y':
            return True
        elif user.upper() == 'N':
            return False
        else:
            print('\nInput invalid. Enter only "Y" or "N"')
            continue


# CRUD Program 

# Writing Sub Program outside the Main Program Function to be able to access the Sub Program from other Function
def readProgram1():
    print('All Python Projects')
    headers = header
    table_data = [[k] + v for k, v in allProject.items()]

    # Print the table
    print(tabulate(table_data, headers=headers, tablefmt="simple"))


def readProgram2():
    print('My Python Projects')
    headers = header
    table_data = [[k] + v for k, v in myProject.items()]

    # Print the table
    print(tabulate(table_data, headers=headers, tablefmt="simple"))

# Giving a parameter to make this function directly usable from other function
def readProgram3(project_code):
    if project_code in allProject.keys():
        print('Project')
        headers = header
        table_data = [[project_code] + allProject[project_code]]

        # Print the table
        print(tabulate(table_data, headers=headers, tablefmt="simple"))
    else:
        print("Project Code not found.")


# 'Read' Program
def program1():
    ui = input('''
Display Options: 
               
1. Display All Python Projects
2. Display My Python Projects
3. Display Project by Project Code
4. Back to Main Directory          
Input : ''')

    # 'Read' Program Controller
    program1Map = {'1' : readProgram1, '2' : readProgram2, '3' : readProgram3}
    # Choosing Back to Main Directory call the returnChecker function
    if ui == '4':
        if returnChecker():
            return
        else:
            program1()
    
    elif ui == '3':
        # Getting the argument for readProgram3 parameter
        project_code = input("Enter Project ID: ")
        readProgram3(project_code)
        program1()

    elif ui in program1Map:
        # Calling the function
        program1Map[ui]()
        program1()
    
    else:
        # Error Checking
        print("Invalid Input, input doesn't match any of the available program directory\n")
        program1()



# 'Create' Program
def program2():
    ui = input('''
Create New Project Options:
               
1. Add New Project to All Python Projects
2. Add Project From All Project to My Python Project
3. Add New Project to My Python Project Manually
4. Back to Main Directory          
Input : ''')
 
    def writeProgram1():
        # Looping until getting the correct Code
        while True:
            index = input(f'Do You want to use 100{len(allProject)} as the New Project Code?? (Y/N) : ')
            if index.upper() == 'Y':
                index = str(1001 + len(allProject))
                break
            elif index.upper() == 'N':
                index = input('Input the Project Code : ')
                if index in allProject.keys():
                    print('Code already used in other Project')
                    continue
                else:
                    break
            else:
                continue

        # Getting the New Value
        content = [
        input('Input the Project name     : '),
        input('Input the Difficulty       : '),
        input('Input Project Duration     : '),
        input('Input Learning Subject     : '),
        input('Input Project Tools        : '),
        input('Input Project Status       : '),
        input("Use today's date?          : ")
        ]

        # Directly Adding new Project to main Dictionary
        allProject[index] = content
        readProgram3(index)
        
        # Checking User to make sure to save with loop
        while True:
            save = input('Do you want to save the change? (Y/N)\nInput : ')
            if save.upper() == 'Y':
                # Just notification as the project already been added before
                print('Project Added!')
                return
            if save.upper() == 'N':
                # Delete the new project so it won't be saved
                del allProject[index]
                print('Project Not Saved!')
                return
            else:
                print('\nInput invalid. Enter only "Y" or "N"')


    def writeProgram2():
        key = input('input Project Code : ')
        # Checking if Code already in My Project
        if key in myProject.keys():
            print('Project is already in My Python Project')
        # Appending Project to My Project
        else: 
            if key in allProject.keys():
                myProject[key] = allProject[key]
                readProgram3(key)
                while True:
                    save = input('Do you want to add this project to My Python Project? (Y/N)\nInput : ')
                    if save.upper() == 'Y':
                        print('Project Added!')
                        return
                    if save.upper() == 'N':
                        del myProject[key]
                        print('Project Not Saved!')
                        return
                    else:
                        print('\nInput invalid. Enter only "Y" or "N"')

            else:
                print("Project Code not found.")
    
    # Same as writeProgram1() just different save location
    def writeProgram3():
        while True:
            index = input(f'Do You want to use 100{len(allProject)} as the New Project Code?? (Y/N) : ')
            if index.upper() == 'Y':
                index = str(1001 + len(allProject))
                break
            elif index.upper() == 'N':
                index = input('Input the Project Code : ')
                if index in allProject.keys():
                    print('Code already used in other Project')
                    continue
                else:
                    break
            else:
                continue
        content = [
        input('Input the Project name     : '),
        input('Input the Difficulty       : '),
        input('Input Project Duration     : '),
        input('Input Learning Subject     : '),
        input('Input Project Tools        : '),
        input('Input Project Status       : '),
        input("Use today's date?          : ")
        ]

        # Save to both dictionary because allProject is the functions as a parent dictionary 
        myProject[index] = content
        allProject[index] = content
        readProgram3(index)
        while True:
            save = input('Do you want to save the change? (Y/N)\nInput : ')
            if save.upper() == 'Y':
                print('Project Added!')
                return
            if save.upper() == 'N':
                del allProject[index]
                del myProject[index]
                print('Project Not Saved!')
                return
            else:
                print('\nInput invalid. Enter only "Y" or "N"')

    # 'Create' program Controller
    program2Map = {'1' : writeProgram1, '2' : writeProgram2, '3' : writeProgram3}
    # Going Back to Main Directory through returnChecker
    if ui == '4':
        if returnChecker():
            return
        else:
            program2()
    elif ui in program2Map:
        # SubFunction calling
        program2Map[ui]()
        program2()
    else:
        # Error Handling
        print("Invalid Input, input doesn't match any of the available program directory\n")
        program2()



# 'Update' Program
def program3():
    ui = input('''
Update Options: 
               
1. Update Project From All Python Project
2. Update Project From My Python Projects
3. Back to Main Directory
Input : ''')
    

    def updateProgram1():
        project_code = input("Enter the Project Code to update: ")
        if project_code in allProject.keys():
            readProgram3(project_code)
            # To Help the User to not have to memorize the value
            header = ['Project', 'Difficulty', 'Duration', 'Learning', 'Tools', 'Status', 'Date']
            x = zip(allProject[project_code], header)
            
            # Looping until getting the correct Code
            while True:
                codeChange = input(f'Current Code is --> {project_code} do you want to change Code? (Y/N) : ')
                if codeChange.upper() == 'Y':
                    key = input('Enter Updated Code number: ')
                    if key in allProject.keys():
                        print('Code is already in use!')
                        continue
                    else:
                        break
                elif codeChange.upper() == 'N':
                    key = project_code
                    break

            content = []
            for i in x:
                print(f'\nCurrent {i[1]} is --> {i[0]}')
                # Showing the Old Value
                update = input(f'Enter updated {i[1]} (Input nothing to keep current value) : ')
                # Option to keep the Old Value
                if update == '':
                    content.append(i[0])
                else:
                    content.append(update)
            
            # Looping until getting clear save input
            while True:
                save = input('Do you want to save the change? (Y/N)\nInput : ')
                if save.upper() == 'Y':
                    print('Project Updated!')
                    del allProject[project_code]
                    allProject[key] = content
                    # Changing the same project if project is in MyProject Dictionary
                    if project_code in myProject.keys():
                        del myProject[project_code]
                        myProject[key] = content
                    return
                if save.upper() == 'N':
                    print('Project Not Changed!')
                    return
                else:
                    print('\nInput invalid. Enter only "Y" or "N"')
            
        else:
            print("Project Code not found.")

    # Similar with the updateProgram1()
    def updateProgram2():
        project_code = input("Enter the Project Code to update: ")
        if project_code in myProject.keys():
            readProgram3(project_code)
            header = ['Project', 'Difficulty', 'Duration', 'Learning', 'Tools', 'Status', 'Date']
            x = zip(myProject[project_code], header)
            print(f'Current Code is --> {project_code}')
            
            while True:
                codeChange = input(f'Current Code is --> {project_code} do you want to change Code? (Y/N) : ')
                if codeChange.upper() == 'Y':
                    key = input('Enter Updated Code number: ')
                    if key in allProject.keys():
                        print('Code is already in use!')
                        continue
                    else:
                        break
                elif codeChange.upper() == 'N':
                    key = project_code
                    break

            content = []
            for i in x:
                print(f'\nCurrent {i[1]} is --> {i[0]}')
                update = input(f'Enter updated {i[1]} (Input nothing to keep current value) : ')
                if update == '':
                    content.append(i[0])
                else:
                    content.append(update)
            
            while True:
                save = input('Do you want to save the change? (Y/N)\nInput : ')
                if save.upper() == 'Y':
                    print('Project Updated!')
                    del allProject[project_code]
                    allProject[key] = content
                    del myProject[project_code]
                    myProject[key] = content
                    return
                if save.upper() == 'N':
                    print('Project Not Changed!')
                    return
                else:
                    print('\nInput invalid. Enter only "Y" or "N"')

        else:
            print("Project Code not found.")
        
    # 'Update' Program Controller
    program3Map = {'1' : updateProgram1, '2' : updateProgram2}
    # Going Back to Main Directory through returnChecker
    if ui == '3':                          
        if returnChecker():
            return
        else:
            program3() 
    # SubFunction calling
    elif ui in program3Map:
        program3Map[ui]()
        program3()
    # Error Handling
    else:
        print("Invalid Input, input doesn't match any of the available program directory\n")
        program3()



# 'Delete' Program
def program4():
    ui = input('''
Delete options:
               
1. Delete Project From All Project
2. Delete Project From My Project
3. Back to Main Directory
               
*(note: "My Project" and "All Project" is connected, all Project in "My Project" is always in "All Project".
        if Project exist in both "My Project" and "All Project", Choosing Option 1 will delete both.
        Choosing Option 2 will only delete Project from "My Project" and not from "All Project").
Input : ''')

    def deleteProgram1():
        # Deleting from AllProject dictionary
        readProgram1()
        id = input('\nInput the Code of the Project You want to Delete : ')
        if id in allProject.keys():
            readProgram3(id)
            # Double Checking with Looping until getting correct option
            while True:
                delete = input('Do you want to Delete this Project? (Y/N)\nInput : ')
                if delete.upper() == 'Y':
                    del allProject[id]
                    print('Project Deleted')
                    # Deleting from Myproject too
                    if id in myProject.keys():
                        del myProject[id]
                    return
                if delete.upper() == 'N':
                    print('Project Not Deleted!')
                    return
                else:
                    print('\nInput invalid. Enter only "Y" or "N"')
        else:
            print("Project Code not found.")
        

    def deleteProgram2():
        # Deleting from MyProject dictionary
        readProgram2()
        id = input('\nInput the Code of the Project You want to Delete : ')
        if id in myProject.keys():
            readProgram3(id)
            # Double Checking with Looping until getting correct option
            while True:
                delete = input('Do you want to Delete this Project? (Y/N)\nInput : ')
                if delete.upper() == 'Y':
                    del myProject[id]
                    print('Project Deleted')
                    return
                if delete.upper() == 'N':
                    print('Project Not Deleted!')
                    return
                else:
                    print('\nInput invalid. Enter only "Y" or "N"')
        else:
            print("Project Code not found.")

    program4Map = {'1' : deleteProgram1, '2' : deleteProgram2}
    # Going Back to Main Directory through returnChecker
    if ui == '3':    
        if returnChecker():
            return
        else:
            program4() 
    # SubFunction calling
    elif ui in program4Map:
        program4Map[ui]()
        program4()
    # Error Handling
    else:
        print("Invalid Input, input doesn't match any of the available program directory\n")
        program4()



# Non CRUD Program

# Details contained inside Dictionary with the same Keys from the Main Data for easy access
details = {
    '1001' : """
Todo List
A command-line application that allows users to manage their tasks. Features include adding new tasks, 
viewing all tasks, marking tasks as complete, deleting tasks, and saving tasks to a file for persistence between sessions.
""",
    '1002' : '''
File Organizer
A script that scans a specified directory, categorizes files based on their extensions, and moves them into corresponding folders. 
It can handle various file types like documents, images, videos, and archives.
''',
    '1003' : '''
News Scraper
A web scraping tool that extracts headlines, summaries, and links from a news website. 
It can save the data to a CSV file or database for further analysis.
''',
    '1004' : '''
CSV Analyzer
A data analysis tool that reads CSV files, performs statistical analysis (mean, median, mode, standard deviation), 
and generates summary reports. It can handle large datasets and provide insights on numerical and categorical data.
''',
    '1005' : '''
Data Visualizer
A graphical tool that creates various types of charts (bar, line, scatter, pie) from data in CSV files. 
It allows users to customize charts and save them as image files.
''',
    '1006' : '''
Spam Classifier
A machine learning model that classifies emails as spam or not spam. 
It uses natural language processing techniques to analyze email content and learns from a labeled dataset.
''',
    '1007' : '''
Notepad App
A desktop application with a graphical user interface for text editing. Features include creating new files, 
opening existing files, saving files, text formatting, and basic editing operations (cut, copy, paste).
''' 
}



def program5():
    ui = input('''
Details: 
1. Get Project Details by Project Code
2. Back to Main Directory
input : ''')
    
    # Going Back to Main Directory through returnChecker
    if ui == '2':
        if returnChecker():
            return
        else:
            program5()

    # Printing the chosen Project Details
    elif ui == '1':
        index = input("Enter Project Code: ")
        if index in details.keys():
            print(details[index])
            program5()
        else:
            print("Project Code not found.")
            program5()
    # Error Handling
    else:
        print("Invalid Input, input doesn't match any of the available program directory\n")
        program5()



# Guides contained inside Dictionary with the same Keys from the Main Data for easy access
guides = {
    '1001' : """
Todo List
Getting started:

- Plan the data structure (e.g., a list of dictionaries for tasks)
- Design the user interface (command-line menu)
- Implement basic CRUD operations (Create, Read, Update, Delete)
- Add file I/O to save and load tasks
- Implement error handling for user inputs
""",
    '1002' : '''
File Organizer
Getting started:

- Research Python's os and shutil modules
- Plan the organization structure (e.g., by file type or date)
- Implement file type detection
- Create a function to move files
- Add logging to track file movements
- Consider handling edge cases (e.g., duplicate file names)
''',
    '1003' : '''
News Scraper
Getting started:

- Choose a news website and analyze its HTML structure
- Learn about requests and BeautifulSoup libraries
- Implement functions to fetch and parse HTML
- Extract relevant information using CSS selectors or XPath
- Design data storage (CSV, database)
- Consider implementing scheduled scraping

''',
    '1004' : '''
CSV Analyzer
Getting started:

- Study Python's csv module and pandas library
- Design functions for different types of analysis
- Implement data loading and basic statistical calculations
- Add data visualization capabilities (e.g., histograms, box plots)
- Consider handling different data types and missing values
- Implement report generation (text or PDF)
''',
    '1005' : '''
Data Visualizer
Getting started:

- Learn matplotlib or seaborn for data visualization
- Design a function to read and process CSV data
- Implement different chart types
- Add customization options (colors, labels, titles)
- Create a user interface for selecting data and chart types
- Implement chart saving functionality
''',
    '1006' : '''
Spam Classifier
Getting started:

- Study basic machine learning concepts and text classification
- Choose a machine learning library (e.g., scikit-learn)
- Prepare a dataset of labeled emails
- Implement text preprocessing (tokenization, stemming)
- Design feature extraction (e.g., bag of words, TF-IDF)
- Train and evaluate different classification models
- Implement a user interface for classifying new emails
''',
    '1007' : '''
Notepad App
Getting started:

- Choose a GUI framework (e.g., PyQt, Tkinter)
- Design the application layout
- Implement basic text editing functionality
- Add file operations (new, open, save, save as)
- Implement text formatting options
- Add keyboard shortcuts for common operations
- Consider adding features like find/replace and word count
''' 
}


def program6():
    ui = input('''Would you like more information on how to get started with these projects?
               
1. Get Project Guides
2. Back to Main Directory
Input : ''')
    
    # Going Back to Main Directory through returnChecker
    if ui == '2':
        if returnChecker():
            return
        else:
            program6()

    # Printing the chosen Project Guides
    elif ui == '1':
        index = input("Enter Project Code: ")
        if index in guides.keys():
            print(guides[index])
            program6()
        else:
            print("Project Code not found.")
            program6()

    # Error Handling
    else:
        print("Invalid Input, input doesn't match any of the available program directory\n")
        program6()



# Dictionary containing URL to get the full guides and see the complete Python Code
url = {
    '1001': 'https://example.com/todo-list',
    '1002': 'https://example.com/file-organizer',
    '1003': 'https://example.com/news-scraper',
    '1004': 'https://example.com/csv-analyzer',
    '1005': 'https://example.com/data-visualizer',
    '1006': 'https://example.com/spam-classifier',
    '1007': 'https://example.com/notepad-app'
}


def program7():
    ui = input('''Would you like to get the full guides and the complete Python Code of the projects from the Web?
               
1. Get the URL
2. Back to Main Directory
Input : ''')
    # Going Back to Main Directory through returnChecker
    if ui == '2':
        if returnChecker():
            return
        else:
            program7()

    # Printing the chosen Project Url
    elif ui == '1':
        index = input("Enter Project Code: ")
        if index in url.keys():
            print(url[index])
            program7()
        else:
            print("Project Code not found.")
            program7()

    # Error Handling
    else:
        print("Invalid Input, input doesn't match any of the available program directory\n")
        program7()



# Main Program Controller
programMap = {'1': program1, '2': program2, '3': program3, '4': program4,
              '5': program5, '7': program7}

while True:
    program = directory()

    if program == '8':
        print('Exiting Program....\nExit')
        break
    # Get put outside the programMap so that the Main Guide is only printed once
    elif program == '6':
        print('''Guides:
For each project, start by breaking down the problem into smaller tasks. Research the necessary libraries and tools. Begin with a basic implementation 
and gradually add features. Don't forget to handle errors and edge cases, and consider user experience throughout the development process.
              ''')
        program6()
    
    # Current Running Program
    elif program in programMap:
        programMap[program]()
    else:
        print("Invalid Input, input doesn't match any of the available program directory")