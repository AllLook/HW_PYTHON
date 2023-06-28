from sys import argv


def _is_leap_year(year):
    return (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def is_valid_date(date):

    month_30 = [4, 6, 9, 11]  # месяца где 30 дней
    mount_31 = [1, 3, 5, 7, 8, 10, 12]  # месяца где 31 день
    day, month, year = map(int, str(date).split('.'))
    if 1 <= year <= 9999 and 1 <= day <= 31 and 1 <= month <= 12:
        if month in month_30 and day > 30:
            return False
        elif month == 2 and not _is_leap_year(year) and day > 28:
            return False
    return True


print(is_valid_date("20.20.1999"))

if __name__ == '__main__':
    date = argv
