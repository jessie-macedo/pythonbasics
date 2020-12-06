#Print even numbers of a list. If x = 40, stops.
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25]

for x in list:
    if x == 20:
         break
    if x % 2 == 1:
      continue
    
    print(x)
