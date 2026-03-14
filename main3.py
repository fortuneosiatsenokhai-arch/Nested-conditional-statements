passing_mark=input("Enter your score: ")
school_fees=input("Enter your payment: ")

if passing_mark>="40":
    if school_fees=="1000":
        print(f"Congratulations on your grading")
    else:
        print("sorry not the right amount needed")
else:
    print("You need to be smarter")