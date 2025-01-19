# enter position and mark x in it location

row1 = ["✅","✅","✅"]
row2 = ["✅","✅","✅"]
row3 = ["✅","✅","✅"]

map =[row1,row2,row3]
print(map)

# desired form

print(f"{row1}\n{row2}\n{row3}\n")

# take position from user

position = input("Position you want to mark as visited eg A2: \n").upper()

letter = position[0]
number = position[1]
print(f"letter: {letter} and number: {number}")
# index() but how
ABC=["A","B","C"]
index_letter = ABC.index(letter)
print(f'the letter is at index {index_letter}')
# convert the number to index
index_number = int(number)-1
print("my numbers.......")
print(index_number)
# using notion of nested list
map[index_letter][index_number] ='❌'
print("chosen position.......")
print(f'{row1}\n{row2}\n{row3}')