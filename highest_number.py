#Given a list of numbers, find the largest number
# 

numbers = [0,6,2,5,6,9]

def get_max(list_input):
    max_value = list_input[0]
    for i in list_input:
        if i > max_value:
            max_value = i
    return max_value
print(get_max(numbers))

# max = numbers[0]

# for i in numbers:
#     if i > max:
#         max = i

# print(max)
