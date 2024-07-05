def squares_of_even_numbers(lst: list) -> list:
    return [x ** 2 for x in lst if x % 2 == 0]

# Example:
if __name__ == "__main__":
    example_list = [1, 2, 3, 4, 5, 6]
    result = squares_of_even_numbers(example_list)
    print(f"Original list: {example_list}")
    print(f"Squares of even numbers: {result}")
