def sort_dict_by_values(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1]))

# Example:
if __name__ == "__main__":
    example_dict = {"a": 3, "b": 1, "c": 2}
    sorted_dict = sort_dict_by_values(example_dict)
    print(f"Original dictionary: {example_dict}")
    print(f"Sorted dictionary: {sorted_dict}")
