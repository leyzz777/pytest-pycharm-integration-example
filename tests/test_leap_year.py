from src.leap_year import check_leap_year

# Testing with leap year
def test_leap_year():
    assert check_leap_year(2000) == "Leap Year"

# Testing with not leap year
def test_not_leap_year():
    assert check_leap_year(2001) == "Not Leap Year"
    assert False
