print("Day one has sumofNumber, evenOrOddCheck")
print("do you want to proceed?")

ifYes = input("Enter Y if yes").strip().lower()

if ifYes=="y":

  print("Sum of two Numbers")

  a= int(input("Enter a:"))
  b= int(input("Enter b:"))

  print("sum of two number is:", a+b)

  print("even numbers check ")

  evenNumberEntered = int(input("Enter number to check even:"))

  if evenNumberEntered%2==0:
    print("this is even number")
  else:
    print("This is odd number")

else:
 print("thank you")