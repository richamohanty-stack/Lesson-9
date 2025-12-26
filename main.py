age=int(input("Enter your age in years: "))

if age>=10 and age<=20:
    print("Your age is in between 10 and 20 years")
    if age>=18:
        print("and you are also eligible to vote.")
    else:
        print("but, you are not eligible to vote.")
else:
    print("Your age is not in between 10 and 20 years")
    if age>=18:
        print("but you are eligible to vote.")
    else:
        print("you are also elibible to vote.")