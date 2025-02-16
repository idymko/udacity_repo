"""
Print Hello World and calculate mean of numpy array.

Author: Dmytro
Date: 16.02.2025

Run in terminal: 
    ipython simple_clean_code.py    
Calculate pylint score: 
    pylint simple_clean_code.py
Perform autocleaning with autopep8: 
    autopep8 --in-place --aggressive --aggressive simple_clean_code.py
"""
import numpy as np

# Main block is run only when the file is run,
# but not when the functions from the file are imported to run in another file.
if __name__ == "__main__":
    print("Hello World!")
    print(np.mean([1, 2, 3, 4]))
