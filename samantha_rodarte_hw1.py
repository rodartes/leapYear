y = int(input("Please enter a year: "))
if y % 4 != 0:
  print("Your year is not a leap year")
elif y % 100 == 0 and y % 400 != 0:
  print("Your year is not a leap year")
else:
  print("Your year is a leap year")