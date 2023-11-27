import core.utils

project_description = '''
Welcome to LECD Electronic Store
=================================================


This project is part of the Introduction to Programming course of the Bachelor on Data Science and Engineering. This project is not part of the evaluation of the course. 

Learning how to program is something that requires time, effort, and, overall, practice. The main purpose of this project is to go beyond the individual exercises that are used in the practical classes. It intends to provide students a slightly larger project to practice the concepts that were introduced over the semester, acquiring familiarity with how a program is built and how multiple parts interact. The tasks that are requested in the context of the project are aligned with overall goals of the bachelor. You will later understand and explore in further detail how the various steps that you will have to implement in this project relate with the major steps required in data science.

The theme of the project is an Electronic Store (a store that sells electronic components). The data that is available for this project comprises different aspects that are related to the operation of an electronic store, all provided as .csv files. The first line of each file contains the headers (i.e., the name of each feature):

	* product_categories.csv - data related to the categories of the products sold by the store
		- id (id of the product category), name (name of the category)
	* products.csv - data related to the products sold in the store, each product can have multiple categories
		- id (id of the product), name (name of the product), price (price of the product), categories (ids of the categories of the product)
	* stores.csv - data related to the stores of the chain
		- id (id of the store), name (name of the physical store), address (address of the store), phone (contact of the store)
	* customers.csv - data related to the customers
		- id (id of the customer), name (name of the customer), nif (NIF of the customer), address (address of the customer), phone (contact of the customer)
	* purchases.csv - data related to the purchases made; the features are:
		- id (id of the purchase), customer_id (id of the customer that did the purchase), store_id (id of the store where the purchase was made), date (date of the purchase), value (value of the overall purchase), product_id (id of the product bought), product_quantiy (quantity of the products bought)
			!! NOTE: for simplicity, we consider that only one product is bought per purchase (although you can aquire multiple items of the same product)

The structure of the application is as follows:

	* program.py - Here is where you will develop all the functionalities required for the project. You have placeholders for each of the expected functionalities. This is the only file where you are expected to work on.
	* interface.py - Includes some basic functionalites to manage the interface. You are not expected to work in this file 
	* utils.py - Includes basic common/generic functionalities. You are not expected to change this code

The program works as a Command Line Interface (CLI). You just need to run the program.py file (e.g., python program.py, or run it within you IDE) and use the command line to interact with the program.

Keep in mind that this is a major simplification of what a real system would look for a similar operational scenario; this is intended solely as the basis to develop the project, and should be seen as such. If you identify any issues with the materials, or if you have suggestions, feel free to pass them along.  

The scope of the project is limited by taking into consideration its purpose. Notwithstanding, if you implement everything that is requested, and are interested in developing further functionalities, we can later identify some (upon explicit request). 

Any questions feel free to get in touch with the professors of the course. 
'''

def start(context):
    """
    Start function of the project. Initializes the menu of the system
    """
    Items = [
        {'name': 'Basic Data Manipulation', 'submenu': [
            {'name': 'Add Product Type', 'callback': getattr(context, 'add_product_type')},
            {'name': 'Add Product', 'callback': getattr(context, 'add_product')},
            {'name': 'Add Client', 'callback': getattr(context, 'add_client')},
            {'name': 'Add Store', 'callback': getattr(context, 'add_store')},
            {'name': 'Add Purchase', 'callback': getattr(context, 'add_purchase')},
            {'name': 'Save Data', 'callback': getattr(context, 'save')},
        ]},

        {'name': 'Report Generation', 'submenu': [
            {'name': 'Generate Report of Sales per Product', 'callback': getattr(context, 'report_of_sales_per_product')},
            {'name': 'Generate Report of Sales per Store', 'callback': getattr(context, 'report_of_sales_per_store')},
        ]},

        {'name': 'Explore Data', 'submenu': [
            {'name': 'Analytical', 'submenu': [
                {'name': 'What is the average spent per client?', 'callback': getattr(context, 'explore_data_average_spent_client')},
                {'name': 'Which client spent the most?', 'callback': getattr(context, 'explore_data_client_most_spent')},
                {'name': 'What product was most bought per month?', 'callback': getattr(context, 'explore_data_best_product_month')},
                {'name': 'Sales per product per month', 'callback': getattr(context, 'explore_data_sales_product_month')},
            ]},
            {'name': 'Graphical', 'submenu': [
                {'name': 'Sales per Month', 'callback': getattr(context, 'explore_data_graphical_sales_month')},
                {'name': 'Sales per Month per Product', 'callback': getattr(context, 'explore_data_graphical_sales_month_product')},
                {'name': 'Correlation Between Price and Sales', 'callback': getattr(context, 'explore_data_graphical_correlation_price_sales')},
            ]},
        ]},
        {'name': 'Help', 'callback': core.interface.help},

    ]

    printMenu('Main Menu', Items)


def help():
    """
    Provides a description of the project
    """
    core.utils.printStatusMessage(core.interface.project_description)
    core.utils.printAcknowledgeMessage()


def printBreadCrumb(breadcrumb):
    """
    Prints a breadcrumb of the navigation of the project
    """
    print(''.join(['-'] * (len(breadcrumb) + 1)))
    print(breadcrumb)
    print(''.join(['-'] * (len(breadcrumb) + 1)) + '\n')

Breadcrumb = ['Initialize']
def printMenu(label, MenuData):
    """
    Generic function to handle the CLI menus
    """
    while True:
        breadcrumb_separator = ' >> '
        breadcrumb = breadcrumb_separator + breadcrumb_separator.join(Breadcrumb)
        printBreadCrumb(breadcrumb)

        print(' ---> ' + label)

        for index, MenuDetails in enumerate(MenuData):
            print(' -----> ' + str(index + 1) + ' - ' + MenuDetails['name'])
        print('')
        print(' -----> 0 - Back')
        print('')

        while True:
            try:
                choice = int(core.utils.printInputMessage('Select an option:'))
            except Exception as e:
                choice = -1

            if choice not in range(len(MenuData) + 1):
                core.utils.printErrorMessage('Invalid selection, please try again', acknowledge=False)
            else:
                break

        consoleClear()

        if choice == 0:
            break
        else:
            choice -= 1  # enumerate from 1 to count items

            if 'callback' in MenuData[choice] and 'submenu' in MenuData[choice]:
                exit(f'Program menu structure is invalid; can either have callback or submenu: {MenuData[choice]}')
            if 'callback' not in MenuData[choice] and 'submenu' not in MenuData[choice]:
                exit(f'Program menu structure is invalid; must have either callback or submenu: {MenuData[choice]}')

            Breadcrumb.append(MenuData[choice]['name'])

            if 'callback' in MenuData[choice]:
                returned = MenuData[choice]['callback']()
                del Breadcrumb[-1]

                if returned == -1:
                    break

            elif 'submenu' in MenuData[choice]:
                printMenu(MenuData[choice]['name'], MenuData[choice]['submenu'])


def consoleClear():
    """
    Helper function to create space ("clear") the console
    """
    print('\n' * 2)
    print('&' * 140)
    print('&' * 140)
    print('&' * 140)
    print('\n' * 2)
    # os.system('cls')
