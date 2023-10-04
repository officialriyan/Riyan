print("Leap year")

year = int(input("Enter a year"))

if year % 4 == 0 :
    print("This is leap year")
elif year % 100 == 0:
    print("This is leap year")
elif year % 400 == 0:
    print("This is leap year")
else:
    print("This is not a leap year")
