la = ['a','e','i','o','u']
letter = input("Введите букву латинского алфавита:")
if la.count(letter):
    letter = 'гласная'
elif letter == 'y':
    letter = 'может быть как гласной , так и согласной'
else:
   letter = 'согласная'
print(f'введенная буква {letter}')