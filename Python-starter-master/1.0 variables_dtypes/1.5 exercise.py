# EXERCISE: LIFE IN A WEEK
# Calculate the numbers of weeks left to leave in your life time [if your expected to leave 90 years]
# hint:52 weeks in a year

age = input("age: ")
ex_Age = input("what syour expected age: ")
yrs_left = int(ex_Age) - int(age)
yrsIn_wks = yrs_left*52
print(f"You are left with {yrs_left} years to leave which is {yrsIn_wks} weeks")