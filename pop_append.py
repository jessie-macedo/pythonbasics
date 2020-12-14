city_list = ["New York", "Fortaleza", "São Paulo", "Toronto", "Tokyo"]
want_to_know = []

index = 0
while index < 5:
    want_to_know.append(city_list.pop())
    index += 1
print(want_to_know)