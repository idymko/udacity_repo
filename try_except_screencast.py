"""
Run in terminal:
    ipython try_except_screencast.py
Calculate pylint score:
    pylint try_except_screencast.py
Perform autocleaning with autopep8:
    autopep8 --in-place --aggressive --aggressive try_except_screencast.py

"""

import pandas as pd
import logging 

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'   
)

def read_data(file_path):
    """
    Prints the content of file if it exits,
    otherwise it throws an exception.

    Args:
        file_path (str): file path

    Returns:
        dataframe: dataframe
    """
    try:
        dataframe = pd.read_csv(file_path)
        logging.info("SUCCESS: There are {} rows in your dataframe".format(df.shape))
        logging.info("SUCCESS: Your file was successfully read in.")
        return dataframe
    except FileNotFoundError:
        logging.error("ERROR: We were not able to find file '%s'", file_path)
        # logging.warning("WARNING: We were not able to find that file %s", file_path)


def enter_int_number():
    try:
        result = int(input("Enter an integer: "))
    except ValueError:
        logging.error("ERROR: Invalid input. Please enter a valid integer.")
    else:
        print("You entered:", result)


def open_file(file_path):
    """
    Opens a file if it exists,
    otherwise it throws an exception.

    Args:
        file_path (str): file path
    """
    try:
        file = open(file_path, "r")
        content = file.read()
    except FileNotFoundError:
        logging.error("ERROR: File not found.")
    else:
        print("File content:", content)
    finally:
        if file:
            file.close()  # Ensuring file is closed even if an exception


def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    # try to return the fraction but if the denominator is zero
    # catch the error and return a string saying:
    # "denominator cannot be zero"
    try:
        fraction_val = numerator / denominator
        return fraction_val
    except ZeroDivisionError:
        logging.error("ERROR: denominator cannot be zero")


def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        n_words: (int) number of words in the string
    '''
    # try to split based on spaces and return num of words
    # but if text isnt a string return "text argument must be a string"
    try:
        n_words = len(text.split(" "))
        return n_words
    except AttributeError:
        logging.error("ERROR: text argument must be a string")


if __name__ == "__main__":
    
    df = read_data("some_path")
    # enter_int_number()
    # open_file("example.txt")
    print("Successful function run:")
    print("Result of division: ", divide_vals(1, 2))
    print(num_words("This is my text, in which we will count a number of words."))

    print("\nException function run:")
    print("Result of division: ", divide_vals(1, 0))
    print("Number of words: ", num_words(1))
