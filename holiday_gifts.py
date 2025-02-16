"""
Contains a function that calculates a total price to be paid out
for gifts based on the input file path that contains the list
of gifts.

Target: meet pep8 standards and receive a 10 score using pylint
# pip install autopep8
# pip install pylint

Run in terminal: 
    ipython holiday_gifts.py
Calculate pylint score: 
    pylint holiday_gifts.py
Perform autocleaning with autopep8: 
    autopep8 --in-place --aggressive --aggressive holiday_gifts.py

Author: Dmytro
Date: 16.02.2025

"""

import numpy as np


def gift_total_price(pth):
    """
    Takes a path and returns the total_price variable.

    Args:
    pth: (str) path to the gift_costs file

    Returns:
    total_price: (float) total price with tax for gifts less than 25
    """
    # open path
    with open(pth, encoding="utf-8") as file:
        gift_costs = file.read().split('\n')

    # change from string to int
    gift_costs = np.array(gift_costs).astype(int)

    # compute total price + tax
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08

    return total_price


if __name__ == "__main__":
    TOTAL_PRICE = gift_total_price('gift_costs.txt')
    print(TOTAL_PRICE)
