#Function: add_numbers
def add_numbers(num1, num2):
    return num1 + num2

#Function: is_even
def is_even(number):
    return number % 2 == 0

#Function: reverse_string 
def reverse_string(text):
    return text[::-1]

#Function: count_vowels 
def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

#Function: calculate_factorial 
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

#Function: apply_decorator 
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator(func):
    return func()

#Sequences
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

#Sets and Dictionaries:
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

#Object-Oriented Programming: Class Creation (2 points)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

# Example usage of the functions:

if __name__ == "__main__":
    # Testing add_numbers
    print(add_numbers(3, 5)) 

    # Testing is_even
    print(is_even(4)) 
    print(is_even(5))  

    # Testing reverse_string
    print(reverse_string("hello")) 

    # Testing count_vowels
    print(count_vowels("OpenAI")) 

    # Testing calculate_factorial
    print(calculate_factorial(5)) 

    # Testing apply_decorator
    def sample_func():
        print("Function Executed")
    apply_decorator(sample_func)

    # Testing sort_by_age
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print(sort_by_age(people))  

    # Testing merge_dicts
    dict1 = {'a': 100, 'b': 200}
    dict2 = {'b': 300, 'c': 400}
    print(merge_dicts(dict1, dict2))  

    # Testing Car class
    my_car = Car("Toyota", "Camry", 2020)
    my_car.display_info() 
