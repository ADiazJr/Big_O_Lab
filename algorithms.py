
#Task 1
# Constant Time: O(1)
def even_or_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(even_or_odd(25))

#Task 2
# Linear Time: O(n)
list_of_numbers = [1,10,50,23,40,50,79,87,93,56,28,91,81,74]
def check_if_100(list_of_numbers):
    for number in list_of_numbers:
        if number > 100:
            return False
    return True

print(check_if_100(list_of_numbers))

#Task 3
# Linear Time: O(n)
list_of_names = ["Kratos", "Atreus", "Brok", "Sindri", "Faye", "Faye"]
def check_names(list_of_names):
    for name in range(len(list_of_names)):
        hold_name = list_of_names.pop(name)
        if hold_name in list_of_names:
                return True
        list_of_names.insert(name, hold_name)
    return False

print(check_names(list_of_names))

#Task 4
# Quadratic Time: O(n^2)
def sort_list(unsorted_numbers):
    sorted = False
    no_change = 0
    while sorted == False:
        for number in range(len(unsorted_numbers)):
            if number < len(unsorted_numbers)-1:
                first_value = unsorted_numbers[number]
                second_value = unsorted_numbers[number+1]
                if first_value > second_value:
                    unsorted_numbers[number] = second_value
                    unsorted_numbers[number+1] = first_value
                else:
                    no_change += 1
        if no_change == len(unsorted_numbers)-1:
            sorted = True
        else:
            no_change = 0
    return unsorted_numbers

sorted_list = sort_list([20001283, 374, 3587, 2384, 239, 5, 403, 48752438975239084, 29, 1, 9834])
print(sorted_list)
