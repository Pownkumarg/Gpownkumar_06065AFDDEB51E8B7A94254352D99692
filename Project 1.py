# Leap year

def tsLeap Year (year):

if(year% 4==0 and year % 100 !=0) or year % 400 == 0:

return True

else:

return False

year =2020

if tsLeap Year(year):

print("{} is a leap year.", format(year)) else:

print(") is not a leap year.", format(year))