def is_leap_year(year):
    """This function can identify if the given year is a leap year or not."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is a leap year."
            else:
                return f"{year} is not a leap year."
        else:
            return f"{year} is not a leap year."    
    else:
        return f"{year} is not a leap year."
    
print(is_leap_year(2012)) 

