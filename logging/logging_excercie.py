"""
Author: Dmytro
Date: 15.03.2025 

# 1. import logging
# 2. set up config file for logging called `results.log`
# 3. add try except with logging for success or error
#    in relation to checking the types of a and b
# 4. check to see that log is created and populated correctly
#    should have error for first function and success for
#    the second
# 5. use pylint and autopep8 to make changes
#    and receive 10/10 pep8 score
#    autopep8 --in-place --aggressive --aggressive logging_excercie.py
#    pylint logging_excercie.py
"""
import logging

logging.basicConfig(
    filename='results.log',
    level=logging.INFO,
    filemode='w',  # a - append, w - write
    datefmt="%Y-%m-%d %H:%M:%S",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

def sum_vals(var1, var2):
    '''
    Args:
        var1: (int)
        var2: (int)
    Return:
        var1 + var2 (int)
    '''
    try:
        # tests
        assert isinstance(var1, int)   # check if variable is int
        assert isinstance(var2, int)   # check if variable is int

        # results
        result = int(var1 + var2)
        logging.info(
            "SUCCESS: Both variables '%s' and '%s' are ints",
            var1, var2)
        return result
    
    except AssertionError:
        logging.error(
            "Variable '%s' if of type %s and '%s' is of type %s",
            var1, type(var1), var2, type(var2))
        return None

if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(4, 5)
    sum_vals(4, 5.)
