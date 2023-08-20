#!/usr/bin/python3

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The calculated average.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list is empty")
    
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average


def main():
    try:
        num_list = [4, 8, 12, 16, 20]
        avg = calculate_average(num_list)
        print(f"The average is: {avg:.2f}")
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()

