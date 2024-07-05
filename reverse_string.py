def reverse_string(s: str) -> str:
    return s[::-1]

# Example :
if __name__ == "__main__":
    sample_string = "hello"
    reversed_string = reverse_string(sample_string)
    print(f"Original string: {sample_string}")
    print(f"Reversed string: {reversed_string}")
