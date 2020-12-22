fantasy_list = ["dragon", "winged serpent", "basilisc", "siren", "pegasus"]

#for species in fantasy_list:
#    print(species)

#Using break to not go through the entire loop.

for species in fantasy_list:
    print(species)
    if species == "basilisc":
        print("They have a basilisc!")
        break

print("While loooooop")

index = 0
while index < len(fantasy_list):
    print(fantasy_list[index])
    index += 1
print("While loooooop end")
#Using continue to avoid some numbers

numbers_list = [1, 2, 9, -3, -5, 6, -9, 7, -25, 30]
for number in numbers_list:
    if number < 0:
        continue
    print(number)

