
def check_leap_year(year:int) -> str:
    """
    Function to check if the given year is a leap year.
    
    Args:
    year: integer

    Returns:
    String "Leap Year" or "Not Leap Year"
    """

    ## Divided by 100 means century year.
    ## And century year divided by 400 means
    if (year % 400 == 0) and (year % 100 == 0):
        return "Leap Year"

    ## Not divided by 100 means not a century year.
    ## Year divided by 4 is a leap year.
    elif (year % 4 == 0) and (year % 100 != 0):
        return "Leap Year"

    ## Not divided by 4 and 400 means not a leap year.
    else:
        return "Not Leap Year"
    

def main(year:int) -> None:
    print(check_leap_year(year))

if __name__ == '__main__':
    main(2000)