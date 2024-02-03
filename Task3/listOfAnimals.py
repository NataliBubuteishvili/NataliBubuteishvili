animal_list = []

for i in range(4):
    animal = input("Enter an animal: ")
    animal_list.append(animal)

print(animal_list)

index = int(input("Enter the index of the animal you want to remove (0,1,2,3): "))

if 0 <= index < len(animal_list):
    print(animal_list[index])
    del animal_list[index]
    print(animal_list)
else:
    print("Invalid Index")