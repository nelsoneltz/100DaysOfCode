def is_leap(year):
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
    
def days_in_month(year,month):
    months_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2:
        return 29
    return months_days[month-1]

year = int(input("Enter Year: "))
month = int(input("Enter month: "))
days = days_in_month(year,month)

print(days)

