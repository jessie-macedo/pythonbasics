#Basic For

print("Printing just numbers...")
for x in range(5):
 print("I love fantasy fiction!")
print("Or maybe I just love escapism...")

print("**************Take your time*********")

dragon = 1
while dragon < 5:
    print("I saw ", dragon, "dragons")
    dragon += 1
print ("Oh my Gosh, this is not normal, run!!!!")

print("**************Take your time*********")

princes = 0
while True:
    print(princes, "Princes")
    princes += 1
    if princes >= 10:
        print("Calm down, that´s to much for one princess to decide...")
        break

print("**************Take your time*********")

for princes in range(10):
    if princes == 5 or princes == 7:
        print("We won´t choose number: ")
        print(princes)
        continue
    print("Prince", princes, "is available")

 
print("**************Take your time*********")

dragons=0
while(dragons < 5):
    print("We have seen", dragons,"today")
    dragons += 1
else:
    print("We have seen", dragons,"dragons in a day, it´s bad news, just take cover...")

