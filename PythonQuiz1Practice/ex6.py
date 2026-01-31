while True:
 year = int(input("Enter a year: "))

 if year > 0:
     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      print(f"{year} is a leap year")
     else:
         print(f"{year} is not a leap year")
         break
 else:
    print("Please enter a valid year")

