# Body Mass Index
# formula = weight/height*height

weight = input("what is your weight in kg: ")
height = input("what is your height in m: ")
weight_to_float=float(weight)
height_to_float=float(height)
# print(round(2/12,2))
x=height_to_float*height_to_float
bmi = weight_to_float/x
print(f'your bmi is {bmi}')

if bmi<18.5:
    print("you are underwight")
elif 18.5<bmi<25:
    print("normal weight")
elif 25<bmi<30:
    print("slightly overweight")
elif 30<bmi<35:
    print("ypu are abessed")
elif 35<bmi<45:
    print("you are clinically obessed")
else:
    print("too bad")