# name = input("enter my name: \n").lower()
# if name=="sebastien":
    # print("correct")
# else:
    # print("wrong name")    

# check if a number is even
# num = int(input("number: "))
# if num%2==0:
    # print("even")
# else:
    # print("odd")

height = float(input("height: "))
age = int(input("age: "))


if height>1.5:
    print("eligible.")
    if age<=14:
        print("under 14")
    elif age<=16:
        print("under 16")
    elif age<=18:
        print("under 18")
        print("age eligible.")
        gender = input("gender: ").capitalize()
        if gender=="FEMALE":
            print("you are selected")
        else:
            print("Females only.")
    else:
        print("you are overage.")
else:
    print("not eligible")
