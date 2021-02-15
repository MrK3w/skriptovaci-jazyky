import math

def sorted_list_of_numbers(new_list):
    x = [x for x in new_list if type(x) == int or type(x) == float]
    x.sort()
    return x

def overlapping(first_list,second_list):
    return len(first_list + second_list) - len(set(first_list + second_list))

def correct_parenthesses(equation):
    stack = 0
    for sign in equation:
        if sign == '(':
            stack += 1
        elif sign == ')':
            stack -=1
        if stack < 0:
            return False
    return stack == 0

def quadratic_equation(inputs):
    a = inputs[0]
    b = inputs[1]
    c = inputs[2]
    result_list = []
    try:
        diskriminant = math.sqrt(b**2 - (4*a*c))
    except: 
        return tuple(result_list)
    if diskriminant == 0:
        result = -b / (2*a)
        result_list.append(result)
        return tuple(result_list)
    elif diskriminant > 0:
        result = (-b-diskriminant)/(2*a)
        result_list.append(result)
        result = (-b+diskriminant)/(2*a)
        result_list.append(result)
        return tuple(result_list)


def count_of_vowels_in_dictionary(sentence):
    sentence = sentence.lower()
    letters_list = ('a','e','i','o','u','y')
    vowels_dictionary = {}
    for letter in sentence:
        if letter in letters_list:
            if letter in vowels_dictionary:
                vowels_dictionary[letter] += 1
            else:
                vowels_dictionary[letter] = 1
    return vowels_dictionary


print(correct_parenthesses("(a+b)/(b*(a+c))"))
print(sorted_list_of_numbers([1,23,4,5,"pes",True,4,4.5]))
print(overlapping([1,2,3,4], [3,4,5]))
print(count_of_vowels_in_dictionary("Technical University"))
print(quadratic_equation((2,-4,2)))