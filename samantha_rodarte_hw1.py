validYear = 0
while validYear == 0:
   y = input("Please enter a valid year: ")
   if y.isdigit():
      validYear = 1
   else:
      print("Invalid input. Try again.")
y = int(y)
if y % 4 != 0:
  print("Your year is not a leap year")
elif y % 100 == 0 and y % 400 != 0:
  print("Your year is not a leap year")
else:
  print("Your year is a leap year")
