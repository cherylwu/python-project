def describe_pet(animal_type, pet_name):
    " " "显示宠物的信息" " "
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')

def describe_pet2(animal_type, pet_name = 'dog'):
    " " "显示宠物的信息" " "
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet2('while')
