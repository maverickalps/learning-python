import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']',':',';','<','>','?','/','.',',','|','~','`']

# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_letters = 5
nr_symbols = 2 
nr_numbers = 2
password_lists = []
for char in range(1, nr_letters + 1):
    password_lists += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password_lists += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_lists += random.choice(numbers)
print(password_lists)
random.shuffle(password_lists)
password_list = ""
for char in password_lists:
    password_list += char

print(f"Your password is : {password_list}")