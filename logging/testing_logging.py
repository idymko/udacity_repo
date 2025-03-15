"""
Author: Dmytro
Date: 15.03.2025

## STEPS TO COMPLETE ##
# 1. import logging
# 2. set up config file for logging called `test_results.log`
# 3. add try except with logging and assert tests for each function
#    - consider denominator not zero (divide_vals)
#    - consider that values must be floats (divide_vals)
#    - consider text must be string (num_words)
# 4. check to see that the log is created and populated correctly
#    should have error for first function and success for
#    the second
# 5. use pylint and autopep8 to make changes
#    and receive 10/10 pep8 score
#    autopep:   autopep8 --in-place --aggressive --aggressive testing_logging.py
#    score:     pylint testing_logging.py
#    run:       ipython testing_logging.py 
"""

import logging

logging.basicConfig(
    filename='test_results.log',
    level=logging.INFO,
    filemode='w',  # a - append, w - write
    datefmt="%Y-%m-%d %H:%M:%S",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    try:
        assert denominator != 0
        assert isinstance(numerator, float)
        assert isinstance(denominator, float)
        logging.info(
            "SUCESS: Denominator is not 0. Numerator and denominator are floats.")
        fraction_val = numerator / denominator
        return fraction_val

    except AssertionError:
        logging.error(
            "Denominator is 0 or numerator/denominator is not float.")
        return None


def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    try:
        assert isinstance(text, str)
        logging.info("SUCCESS: Text is string.")
        n_words = len(text.split())
        return n_words

    except AssertionError:
        logging.error("Text argument must be a string.")
        return None


if __name__ == "__main__":
    divide_vals(3.4, 0)
    divide_vals(4.5, 2.7)
    divide_vals(-3.8, 2.1)
    divide_vals(1, 2)
    num_words(5)
    num_words('This is the best string')
    num_words('one')
