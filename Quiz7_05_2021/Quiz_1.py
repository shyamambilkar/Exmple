my_first_list = []
my_second_list = []

num_1 = int(input("How many Elements you want to sort: "))
for i in range(0,num_1):
    first_list = int(input("Enter Element on list one: "))
    my_first_list.append(first_list)
    # print(my_first_list)

num_2 = int(input("How many Elements you want to sort (List2): "))
for i in range(num_2):
    second_list = str(input("Enter Element on list Two: "))
    my_second_list.append(second_list)
    # print(my_second_list)

pairs = zip(my_first_list, my_second_list)

sorted_pairs = sorted(pairs)

result = [item[1] for item in sorted_pairs]


print("After sorting Result are: ", result)