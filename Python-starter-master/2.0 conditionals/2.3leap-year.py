# if a year is divisible by 4 and not divisible by 100  it is a leap year
# unless the year is also divisible by 400

year = int(input("what year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it is a leap year.")
        else:
            print("not a leap year")
    else:
        print("leap year.")
else:
    print("not a leap year")