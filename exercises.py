from functools import partial
import time
from typing import Callable


num_list = [1, 2, 3, 4, 5] # will be used across multiple exercises


# Exercise: Use the map function along with a lambda function to square each element in a list.
def square_list(numbers: list) -> list:
    return list(map(lambda number: number * number, numbers))

# example usage
print(square_list(numbers=num_list)) # should be [1, 4, 9, 16, 25]


# Exercise: Use the filter function with a lambda function to extract even numbers from a list.
def filter_even(numbers: list) -> list:
    return list(filter(lambda number: number % 2 == 0, numbers))

# example usage
print(filter_even(numbers=num_list)) # should be [2, 4]


# Exercise: Implement a function using reduce to find the product of all elements in a list.
def reduce(callback: Callable, array: list):
    if not array:
        raise(ValueError("can't reduce empty list."))

    if len(array) == 1:
        return array[0]

    rest_result = reduce(callback, array[1:])
    return callback(array[0], rest_result)

def product_of_list(numbers: list) -> list:
    get_product = lambda x, y: x * y
    return reduce(callback=get_product, array=numbers)

# example usage
print(product_of_list(numbers=num_list)) # should be 120


# Exercise: Rewrite a simple for loop that generates a list of squares using list comprehension.
def for_loop():
    squares_list = []
    for i in range(5):
        squares_list.append(i ** 2)
    return squares_list # [1, 4, 9, 16, 25]

def list_comprehension():
    return [number * number for number in range(5)]

# example usage
print(for_loop()) # should be [1, 4, 9, 16, 25]
print(list_comprehension()) # should be [1, 4, 9, 16, 25]


# Exercise: Create a function that takes a tuple of numbers and returns a new tuple with each element squared.
def square_tuple(numbers: tuple) -> tuple:
    square_value = lambda x: x * x
    return tuple(map(square_value, numbers))

# example usage
print(square_tuple(numbers=(1, 2, 3, 4, 5))) # should be (1, 4, 9, 16, 25)


# Exercise: Write a recursive function to calculate the factorial of a number.
def get_factorial(number: int) -> int:
    if number == 1:
        return number
    
    rest_result = get_factorial(number - 1)

    return rest_result * number

# example usage
print(get_factorial(5)) # should be 120


# Exercise: Implement a function that takes another function as an argument and applies it to a list of numbers.
def first_class_function(callback: Callable, array: list) -> list:
    return list(map(callback, array))


print(first_class_function(lambda x: x + 2, num_list))

# Exercise: Create a closure that generates a sequence of numbers starting from a given value.
def start_sequence(start: int):
    def create_sequence(size: int):
        next = start + size

        if size == 1:
            return (next,)
        
        return (create_sequence(size - 1)) + (next,)

    return create_sequence

sequence = start_sequence(start=5)
print(sequence(size=3)) # should be [5, 6, 7]


# Exercise: Define a simple decorator to measure the execution time of a function.
def time_execution(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"this function took {end - start} seconds to be executed")
        return result
    return wrapper

@time_execution
def sleep_for(seconds: int):
    time.sleep(seconds)


sleep_for(seconds=1)


# Exercise: Use the functools.partial function to create a specialized version of an existing function.
def power_of(base: int, exponent: int) -> int:
    if exponent == 1:
        return base
    
    accumulated = base * power_of(base, exponent - 1)

    return accumulated

square_of = partial(power_of, exponent=2)

print(square_of(5))