my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)  # Insert 15 at index 1 (second position)

my_list.extend([50, 60, 70])

my_list.pop()  # Remove the last element

my_list.sort()

index_30 = my_list.index(30)
print(index_30)