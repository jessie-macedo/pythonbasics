Nested_list = [["Dragon", 20], ["Basilisc", 1], ["Pegasus", 3]]
count = 0
for kind in Nested_list:
    for many in kind:
        if type(many) == str:
            print(many)
            continue
        count += many
        print(count)
print(count)

count = 0
for kind in Nested_list:
    for many in kind:
        if type(many) != str:
            count += many
            print(count)
print(count)