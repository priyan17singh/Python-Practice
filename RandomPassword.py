import  random

letter = ["a","b","c","d","e","f"]
numbers = ["1","2","3","4","5","6","7","8","9"]
symbols = [".","!","?"]

length=int(input("How long would you like your password to be? \n"))

pass_list = []

for i in range(len(letter)):
    pass_list.append(random.choice(letter))
for i in range(len(numbers)):
    pass_list.append(random.choice(numbers))
for i in range(len(symbols)):
    pass_list.append(random.choice(symbols))

# print(pass_list)
password =" "
for i in range(length):
    password+=random.choice(pass_list)
print("Your Password is:",password)