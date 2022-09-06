
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
#
def sort_list(unsorted_numbers):
    while (unsorted_numbers[0] != min(unsorted_numbers)) or (unsorted_numbers[-1] != max(unsorted_numbers)):
        for number in range(len(unsorted_numbers)):
            first_value = unsorted_numbers.pop(number)
            if number < len(unsorted_numbers):
                if first_value > unsorted_numbers[number]:
                    unsorted_numbers.insert(number+1, first_value)
                else:
                    unsorted_numbers.insert(number, first_value)
        unsorted_numbers.insert(number, first_value)
    return unsorted_numbers
sorted_list = sort_list([3,5,2,78,6,9])
print(sorted_list)
