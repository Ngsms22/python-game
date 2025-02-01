name1 = input("name 1: ")
name2 = input("name 2: ")
combine_names= name1+name2
t=combine_names.count("t")
r=combine_names.count("r")
u=combine_names.count("u")
e=combine_names.count("e")

add_true = t+r+u+e
print(add_true)
l=combine_names.count("l")
o=combine_names.count("o")
v=combine_names.count("v")
e=combine_names.count("e")

add_love=l+o+v+e
print(add_love)
lov_score = (f"{add_true}{add_love}")
love_score = int(lov_score)
print(love_score)
if love_score>50:
    print("fair enough")
elif love_score>60:
    print("great love count")
elif love_score>70:
    print("cool")
elif love_score>80:
    print("great match.")
elif love_score>90:
    print('''match is perfect.\n
          Romeo and juliet.''')
else:
    print("match not the best")        
