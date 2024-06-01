def turn_around_word (word):
    for char in  range (len(word) -1, -1, -1):
        print(word[char])


word = input("Ingrese una frase")
turn_around_word(word)