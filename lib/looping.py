#!/usr/bin/env python3
def happy_new_year():
    # code goes here!
    pass
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")


happy_new_year()

# pass


def square_integers(int_list):
    # code goes here!
    pass
    squared_list = []
    for num in int_list:
        squared_list.append(num**2)
    return squared_list


# Example usage
input_list = [1, 2, 3, 4, 5]
squared_result = square_integers(input_list)
print("Squared list:", squared_result)


def fizzbuzz():
    # code goes here!
    pass
    for num in range(1, 101):
        print(fizz_buzz(num))


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


fizzbuzz()