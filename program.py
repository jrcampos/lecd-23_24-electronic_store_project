import sys

import core.interface
import core.utils

@core.utils.static_vars(data=None)
def load():
    """
    Loads data from file if it not yet loaded.
    Otherwise, it will return a static variable containing the data previously loaded.

    :param: No parameters.
    :return: A dictionary with the loaded data
    :rtype: dictionary
    """

    print('TODO: implement load\n\n')

    if load.data == None:
        # first time this function is called, load the data
        load.data = {}

        # Load customers data from customers.csv; you can also use dictionaries, see what is best
        Customers = []
        load.data['customers'] = Customers

        # Load stores data from stores.csv; you can also use dictionaries, see what is best
        Stores = []
        load.data['stores'] = Stores

        # Load products categories data from product_categories.csv; you can also use dictionaries, see what is best
        ProductCategories = []
        load.data['product_categories'] = ProductCategories

        # Load products data from products.csv; you can also use dictionaries, see what is best
        Products = []
        load.data['products'] = Products

        # Load purchases data from purchases.csv; you can also use dictionaries, see what is best
        Purchases = []
        load.data['purchases'] = Purchases

    return load.data



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


def add_client():
    """
    Adds a client to the list of clients (in memory).
    Get the details from the user using input(). Properly validate and cast all necessary inputs.

    Provide output to the user through print() statements.
    """

    print('TODO: implement add_client\n\n')
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
    Save the report to a file. Include relevant details such as average sales number/value per month, average number of clients, ....
    """

    print('TODO: implement report_of_sales_per_store\n\n')
    pass


'''
Explore Data menu functions   
'''

'''
Explore Data --> Analytical menu functions   
'''
def explore_data_average_spent_client():
    """
    Compute what is the average spent overall by clients and the standard deviation.

    Provide output to the user through print() statements.
    """

    print('TODO: implement explore_data_average_spent_client\n\n')
    pass


def explore_data_client_most_spent():
    """
    Identify the client (include the name, NIF, ..., details) that overall spent more.
    This endpoint is similar to the previous, avoid duplicating code.

    Provide output to the user through print() statements.
    """

    print('TODO: implement explore_data_client_most_spent\n\n')
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
