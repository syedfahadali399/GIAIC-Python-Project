days_per_year: int = 365
hours_per_day: int = 24
min_per_hour: int = 60
sec_per_min: int = 60

def main():
    print(f"There are {days_per_year * hours_per_day * min_per_hour * sec_per_min} seconds in a year!")

main()