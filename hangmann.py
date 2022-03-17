list1 = []
from random import choice
guessed = False
guessed_letters = []
guessed_words = []
tries = 8 

word1 = input('Kérlek add meg az első szót!:')

list1.append(word1)

word2 = input('Kérlek add meg a második szót!:')

list1.append(word2)

word3 = input('Kérlek add meg a harmadik szót!:')

list1.append(word3)

word4 = input('Kérlek add meg a negyedik szót!:')

list1.append(word4)

word5 = input('Kérlek add meg az ötödik szót!:')

list1.append(word5)

print('A szavak amiket megadtál: ', list1,)


random_choice = choice(list1)
print(random_choice)

word_hossz = "_" * len(random_choice)


print(word_hossz)
print("\n")

while not guessed and tries > 0:
    guess = input("Kérlek tippelj egy betüt vagy szót:").upper()
    if len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("Már választottad ezt a betüt", guess)
        elif guess not in guessed_letters:
            print(guess, "Nincs benne a szóban,")
            tries -= 1
            guessed_letters.append(guess)
        else:
            print("Ügyes!,", guess , "benne van a szóban!")
            guessed_letters.append(guess)
            
            
    elif len(guess) == len(random_choice) and guess.isalpha():
        if  guess in guessed_words:
            print("Már tippelted ezt a szót", guess)
        elif guess not in guessed_words:
            print(guess, "nincs a szóba.")
            tries -= 1
            guessed_words.append(guess)
        else:
            guessed = True
            word_hossz = random_choice


    else:
        print("Nem megfelelő formátumú tipp")
        print(word_hossz)
        print("\n")


if guessed:
    print("Gratulálok, eltaláltad a szót! Nyertél!")
else:
    print("Sajnálom, nincs több próbálkozásod, a szó a",random_choice,"volt.","Talán máskor.")





