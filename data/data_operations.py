# data_operations.py

def sum_numbers(numbers):
    return sum(numbers)

def find_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

def count_occurrences(data_list, item):
    return data_list.count(item)

def sort_numbers(numbers):
    return sorted(numbers)

def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)
