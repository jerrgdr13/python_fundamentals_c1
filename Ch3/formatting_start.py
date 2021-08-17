#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  today = datetime.now()

  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  #print(today.strftime("The current year is : %Y"))
  #print(today.strftime("%a, %d, %B, %y"))


  # %c - locale's date and time, %x - locale's date, %X - locale's time
  #print(today.strftime("Locale date and time: %c"))
  #print(today.strftime("Locale date and time: %x"))
  #print(today.strftime("Locale date and time: %X"))


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(today.strftime("Current time: %I:%M:%S:%p"))
  print(today.strftime("24-hour time: %H:%M"))

if __name__ == "__main__":
  main();
