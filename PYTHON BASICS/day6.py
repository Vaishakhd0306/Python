print("Age Predictor: ")

while True:
 enteredAge = input("Please enter your year of birth:").strip()

 if enteredAge.isdigit():
  year = int(enteredAge)
  if 1900<=year<=2026:
     break
  else:
     print("invalid Age")
 else: 
  print("Please enter numbers only") 

print("Your age is",2026-year)
