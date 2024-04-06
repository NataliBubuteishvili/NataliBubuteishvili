animal_list = []

for i in range(4):
    animal = input("Enter an animal: ")
    animal_list.append(animal)

print(animal_list)

index = int(input("Enter the index of the animal you want to remove (0,1,2,3): "))  # +1 ინდექსით უნდა დაბეჭდო

if 0 <= index < len(animal_list):
    print(animal_list[index]) #  -1 ინდექსად უნდა დაბეჭდო 
    del animal_list[index]  #  -1 ინდექსზე უნდა წაშალო
    print(animal_list)
else:
    print("Invalid Index")
