

def new_list (size: int):
    list_ = []
    for i in range(size):
        list_.append(i)
    return list_

my_list = new_list(10)

def my_shuffle(my_list: list):
    for i in range(len(my_list)):
        ni = random.randint(0, len(my_list)-1)
        my_list.append(my_list.pop(ni))

print(my_list)
my_shuffle(my_list)
print(my_list)
