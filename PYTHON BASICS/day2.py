marks = int(input("enter the marks"))
if marks>=85:
    print("passed with distinction")
elif 85>marks>=70:
    print("passed with first class")
elif(70>marks>=60):
    print("passed with second class")
elif(marks<60 & marks>=30):
    print("passed with first class")   
else:
    print("retry")        