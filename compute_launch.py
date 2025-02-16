"""
Before you begin, make sure to run this command in your terminal to install pytest:
* pip install -U pytest

Then, to run pytest, just enter:
* pytest

Right now, not all of the tests should pass. 
Fix the function to pass all its tests! 
Once all your tests pass, try writing some additional unit tests of your own!
"""
def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    return launch_day - current_day
