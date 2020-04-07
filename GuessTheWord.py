import random

words_list = ("арбуз", "баран", "волк", "гранат", "дракон", "енот", "живот", "зонт", "самолет", "шайба", "весна")

secret_word = random.choice(words_list)

# print(secret_word)

gamer_word = ["*"] * len(secret_word)

print("".join(gamer_word))

errors_counter = 0

while True:
    letter = input("Введите ОДНУ русскую букву: ").lower()
    if len(letter) != 1:
        continue
    #print(letter)
    
    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            if symbol == letter:
                  gamer_word[idx] = symbol
        if "*" not in gamer_word:
            print("Вы выиграли!")
            print("Было загадано слово: ", secret_word.upper())
            break
    else:
        errors_counter += 1
        print("Ошибок допущено ", errors_counter)
        if errors_counter == 8:
            print("Вы проиграли")
            break
    print("".join(gamer_word))
    