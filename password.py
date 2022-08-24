import random
import string

print('Serdecznie witamy w naszym generatorze!')

length = int(input("Jak długie hasło Państwo sobie życzą? "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

string_with_all_characters = lower + upper + num + symbols

temp = random.sample(string_with_all_characters,length)
password = "".join(temp)

print('Serdecznie witamy w naszym generatorze!')
print(password)