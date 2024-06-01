import json

def variable_consult (variable):
    while True:
        try:
            value_output = int(input(f"Please enter the {variable} value of de pokemon: "))
            break
        except ValueError:
            print("Invalid input, please enter a valid value.")
    return value_output

def user_consult ():
    poke_name = input("Please, enter the name of the POKEMON: ")
    
    try:
      valid_types = ["fire", "wind", "water", "earth"]
      while True:
          poke_type = input("Please, enter the type of POKEMON: ")
          if poke_type.lower() in valid_types:
              break
          else:   
           input("Invalid input, enter a correct type, press enter to continue.")
    except ValueError as ex:
      print (ex)
      while poke_type.lower() in valid_types:
       input("Invalid input, enter a correct type, press enter to continue.")
       poke_type = input("Please, enter the type of the POKEMON: ")

    poke_hp = variable_consult("HP")
    poke_attack = variable_consult("attack")
    poke_defense = variable_consult("defense")
    poke_sp_attack = variable_consult("Sp.Attack")
    poke_sp_defense = variable_consult("Sp.Defense")
    poke_speed = variable_consult("speed")

    return  {
      "name": {
        "english": poke_name
      },
      "type": [
        poke_type
      ],
      "base": {
        "HP": poke_hp,
        "Attack": poke_attack,
        "Defense": poke_defense,
        "Sp. Attack": poke_sp_attack,
        "Sp. Defense": poke_sp_defense,
        "Speed": poke_speed
      }
    }
    
def json_read_write (file1,  file2):
    data_to_add = user_consult()
    print(data_to_add)
    with open (file1, "r" ) as file_to_read:
         file_json_convert_to_string = json.load (file_to_read)
         file_json_convert_to_string.append(data_to_add)
    with open(file2, "w") as file_to_write:
        json.dump(file_json_convert_to_string, file_to_write, indent =1 )


json_read_write("1.json", "2.json")