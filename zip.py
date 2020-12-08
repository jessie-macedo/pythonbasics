#Just learning to use zip
styles = ['Red', 'Blue', 'Smily']
beasts  = ['Dragon', 'Basilisc', 'Flower']
how_many = [1,2,3]

full_beasts = zip(styles, beasts, how_many)

list_beasts = list(full_beasts)
print(list_beasts)
