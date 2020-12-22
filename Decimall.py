# Import Decimal below:
from decimal import Decimal 

# Fix the floating point math below:
test1= Decimal('0.1') + Decimal('0.20')
print(test1)

test2 = Decimal('0.30') * Decimal('0.40')
print(test2)

print("No decimal")

print(0.1 + 0.20)
print(0.30 * 0.40)