range_start=int(input("You want to start from: "))

range_end=int(input("You want to end at: "));


# RUNNING OUR FOR LOOP HERE:
for x in range(range_start, range_end):
    if x%3!=0 and x%5!=0:
        print(x)
    elif x%3==0 and x%5==0:
        print("fizzbuzz")
    elif x%3==0:
        print("fizz")
    elif x%5==0:
        print("buzz")

