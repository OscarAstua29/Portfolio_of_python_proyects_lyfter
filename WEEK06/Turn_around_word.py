def turn_around_word (world):
    for char in  range (len(world) -1, -1, -1):
        print(world[char])


world = input("Ingrese una frase")
turn_around_word(world)