import sys

import core.interface
import core.utils


def load_customers():
    """
    Loads customers from a file and returns a list of them.
    """

    # Load customers data from customers.csv; you can also use dictionaries, see what is best
    with open('data/customers.csv') as f:
        customers = f.readlines()

    return customers


def load_stores():
    """
    Loads stores from a file and returns a list of them.
    """

    print('TODO: implement load_stores\n\n')

    # Load stores data from stores.csv; you can also use dictionaries, see what is best
    pass


def load_products_categories():
    """
    Loads products categories from a file and returns a list of them.
    """

    print('TODO: implement load_stores\n\n')

    # Load products categories data from products_categories.csv; you can also use dictionaries, see what is best
    pass


def load_products():
    """
    Loads products from a file and returns a list of them.
    """

    print('TODO: implement load_products\n\n')

    # Load products data from products.csv; you can also use dictionaries, see what is best
    pass


def load_purchases():
    """
    Loads purchases from a file and returns a list of them.
    """

    print('TODO: implement load_purchases\n\n')

    # Load stores data from purchases.csv; you can also use dictionaries, see what is best
    pass


def load_data():
    """
    Loads all data from files and returns it in a dictionary where the keys are
    data type e and the values are a list of that data. The dictionary keys are:
    customers, stores, product_categories, products, and purchases.

    :param: No parameters.
    :return: A dictionary with the application data
    :rtype: dictionary
    """
    data = {}

    data['customers'] = load_customers()
    data['stores'] = load_stores()
    data['product_categories'] = load_products_categories()
    data['products'] = load_products()
    data['purchases'] = load_purchases()

    return data


@core.utils.static_vars(data=None)
def database():
    """
    Returns the application database

    Loads the data if it is not already loaded and populates the database in memory.
    Otherwise, it will return the database in memory.

    See load_data() function.

    :param: No parameters.
    :return: A dictionary with the application data
    :rtype: dictionary
    """

    # first time this function is called, load the data
    if database.data == None:
        database.data = load_data()

    return database.data


'''
Basic Data Manipulation menu functions  
'''
def add_product_type():
    """
    Adds a product type to the list of products (in memory).
    Get the details from the user using input(). Properly validate and cast all necessary inputs.

    Provide output to the user through print() statements.
    """

    print('TODO: implement add_product_type\n\n')
    pass


def add_product():
    """
    Adds a product to the list of products (in memory).
    Get the details from the user using input(). Properly validate and cast all necessary inputs.

    Provide output to the user through print() statements.
    """

    print('TODO: implement add_product\n\n')
    pass


def add_store():
    """
    Adds a store to the list of stores (in memory).
    Get the details from the user using input(). Properly validate and cast all necessary inputs.

    Provide output to the user through print() statements.
    """

    print('TODO: implement add_store\n\n')
    pass


def list_customers():
    """
    Shows all customers in the default output
    """
    data = database()

    print('TODO: redo list_customers to be a prettier presentation\n\n')

    for c in data['customers']:
        print(c)


def add_customer():
    """
    Adds a customer to the list of customers (in memory).
    Get the details from the user using input(). Properly validate and cast all necessary inputs.

    Provide output to the user through print() statements.
    """

    print('TODO: implement add_customer\n\n')
    pass


def add_purchase():
    """
    Adds a purchase to the list of purchases (in memory).
    Get the details from the user using input(). Properly validate and cast all necessary inputs.

    Provide output to the user through print() statements.
    """

    print('TODO: implement add_purchase\n\n')
    pass


def save():
    """
    Save the data to persistent storage.
    Subsequent loads of data should use the most recent data available.
    """

    print('TODO: implement save\n\n')
    pass


'''
Report Generation menu functions   
'''
def report_of_sales_per_product():
    """
    Generates the report of overall sales per product.
    Save the report to a file. Include relevant details such as average sales, average value, average quantity, ... .
    """

    print('TODO: implement report_of_sales_per_product\n\n')
    pass

def report_of_sales_per_store():
    """
    Generates the report of sales per store.
    Save the report to a file. Include relevant details such as average sales number/value per month, average number of customers, ....
    """

    print('TODO: implement report_of_sales_per_store\n\n')
    pass


'''
Explore Data menu functions   
'''

'''
Explore Data --> Analytical menu functions   
'''
def explore_data_average_spent_customer():
    """
    Compute what is the average spent overall by customers and the standard deviation.

    Provide output to the user through print() statements.
    """

    print('TODO: implement explore_data_average_spent_customer\n\n')
    pass


def explore_data_customer_most_spent():
    """
    Identify the customer (include the name, NIF, ..., details) that overall spent more.
    This endpoint is similar to the previous, avoid duplicating code.

    Provide output to the user through print() statements.
    """

    print('TODO: implement explore_data_customer_most_spent\n\n')
    pass


def explore_data_best_product_month():
    """
    What product sold the most per month.

    Provide output to the user through print() statements.
    """

    print('TODO: implement explore_data_best_product_month\n\n')
    pass


def explore_data_sales_product_month():
    """
    Compute the sales per month per product.

    Provide output to the user through print() statements.
    """

    print('TODO: implement explore_data_sales_product_month\n\n')
    pass


'''
Explore Data --> Graphical menu functions   
'''
def explore_data_graphical_sales_month():
    """
    Plot the number of sales per month. You can use a bar plot or line plot.
    This function should ask the user how many past months to consider.

    Bar plot: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
    Line plot: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

    Use matplotlib to generate the plots. Explore its documentation.
    You can also use seaborn module to generate better looking plots (https://seaborn.pydata.org/index.html)
    """

    print('TODO: implement explore_data_graphical_sales_month\n\n')
    pass

def explore_data_graphical_sales_month_product():
    """
    Create a line plot for the number of sales per product per month (i.e., a line plot with a line for each plot)
    The data used for this endpoint is similar to the one used in explore_data_sales_product_month. Avoid duplicating code.

    Line plot: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

    Use matplotlib to generate the plots. Explore its documentation.
    You can also use seaborn module to generate better looking plots (https://seaborn.pydata.org/index.html)
    """

    print('TODO: implement explore_data_graphical_sales_month_product\n\n')
    pass

def explore_data_graphical_correlation_price_sales():
    """
    Create a scatter plot that allows understanding the correlation between the prices of product and its sales.

    Scatter plot: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

    Use matplotlib to generate the plots. Explore its documentation.
    You can also use seaborn module to generate better looking plots (https://seaborn.pydata.org/index.html)
    """

    print('TODO: implement explore_data_graphical_correlation_price_sales\n\n')
    pass


if __name__ == '__main__':
    core.interface.start(sys.modules[__name__])
