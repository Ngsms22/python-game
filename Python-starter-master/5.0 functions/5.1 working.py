# # functions in python

# def greet():
#     print("Hello")
#     print("nice start")
# greet()

# def bmi_calculator():
#     weight = input("what is your weight in kg: ")
#     height = input("what is your height in m: ")
#     weight_to_float=float(weight)
#     height_to_float=float(height)
# # print(round(2/12,2))
#     x=height_to_float*height_to_float
#     bmi = weight_to_float/x
#     print(f'your bmi is {bmi}')

#     if bmi<18.5:
#         print("you are underwight")
#     elif 18.5<bmi<25:
#         print("normal weight")
#     elif 25<bmi<30:
#         print("slightly overweight")
#     elif 30<bmi<35:
#         print("ypu are abessed")
#     elif 35<bmi<45:
#         print("you are clinically obessed")
#     else:
#         print("too bad")
# bmi_calculator()

# def sum_odd():
#     limit = int(input("whats ur limit: \n"))
#     sum = 0
#     i=1
#     while i<limit:
#         sum = sum +i
#         i=i+2
#     print(sum)
# sum_odd()



# def check_prime():
#     number= int(input("enter number to check"))
#     if number%2==0:
#         print("not prime")
#     elif number%1==0 and number%number==0:
#         print("prime.")
# check_prime()
    

# fxn to take in your age,school,department and print a story based on that 

def band_name(i,x,y,z):
    print(f'you are {age} years old and you are schooling in {school} in the department of {department}')
name=input("Enter your name: \n")
age=input("Enter your age: \n")
school=input("enter your school: \n")
department=input("Enter your department: \n")

band_name(name,age,school,department)