def convert_minutes_to_days(total_mins):
    days = total_mins // 1440
    extra_minutes = total_mins % 1440

    hours = extra_minutes // 60
    minutes = extra_minutes % 60

    print(f"{total_mins} = {days} days, {hours} hours, and {minutes} minutes")

def printconvert():
    convert_minutes_to_days(30)

if __name__ == "__main__":
  printconvert()