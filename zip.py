#Just learning to use zip
styles = ['Red', 'Blue', 'Winged']
beasts  = ['Dragon', 'Basilisc', 'Leopard']
#how_many = [1,2,3]

#full_beasts = zip(styles, beasts, how_many)
full_beasts = zip(styles, beasts)

list_beasts = list(full_beasts)
print(list_beasts)

#Append - Nested List
list_beasts.append(('Dark', 'Elf'))
print(list_beasts)

print(list_beasts[3])

##Testing some usesof lists
print("First two elements of the list")
print(list_beasts[:2])
print("Last two elements of the list")
print(list_beasts[2:])
print("Selecting some elements")
print(list_beasts[1:3])
print("How many Elves do we have?")
print(beasts.count("Leopard"))