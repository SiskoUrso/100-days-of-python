def is_leap_year(year):
    """
    Determines if a year is a leap year.

    A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
is_leap_year(1981)