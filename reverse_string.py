def reverse_string(s: str) -> str:
    return s[::-1]

# Example :
if __name__ == "__main__":
    example_string = "hello"
    reversed_string = reverse_string(example_string)
    print(f"Original string: {example_string}")
    print(f"Reversed string: {reversed_string}")
