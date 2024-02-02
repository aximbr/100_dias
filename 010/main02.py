#Check if a year is a leap year or not
def is_leap(year_test_in):
    """return True if the year is a leap year."""
    if (year_test_in%4 == 0):
        if (year_test_in%100 == 0):
            if (year_test_in%400 == 0):
                return True
            else: 
                return False
        else:
            return True    
    else:
        return False

def days_in_month(year_in, month_in):
    """returns number of days of a month, check also
    if is a leap year"""
    if month_in == 2 and is_leap(year_in):
        return 29
    else:
        days_month = [31, 28 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_month[month_in -1]
    
#main()
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
