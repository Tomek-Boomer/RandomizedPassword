import random
import string

print('Serdecznie witamy w naszym generatorze haseł!')

length = int(input("Jak długie hasło Państwo sobie życzą (min.4 znaki prosimy)? "))
if length < 4:
    print("O kurcze! O nie! Miało być mniej niż 4 znaki!")
else:
    length2 = length - 4 # Odejmuję 4 znaki, które będą musiały być unikalne, a niżej definiuję typy stringów
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    # Przechodzimy do losowania po jednym elemencie z każdego koszyka

    lower2 = random.sample(lower,1)
    upper2 = random.sample(upper,1)
    num2 = random.sample(num,1)
    symbols2 = random.sample(symbols,1)

    # Dodajemy nasze 4 elementy z każdego typu znaku oraz resztę dowolnie

    at_least_one = lower2 + upper2 + num2 + symbols2
    string_with_all_characters = lower + upper + num + symbols

    temp2 = random.sample(at_least_one,4) # randomizujemy nasze 4 różne znaki - po 1 z każdego typu
    temp = random.sample(string_with_all_characters,length2) # randomizujemy pozostałe znaki
    temp3 = random.sample(temp+temp2,length) # dodatkowa randomizacja (aby 4 różne znaki nie były zawsze na początku)
    password = "".join(temp3)

    print("Twoje nowe hasło to: " + password)