# FizzBuzz

def fizz_buzz(numbers):
    """
    Fizz Buzz

    Checks if each number in an List is divisible by 3 and 5, 3 or 5 and replaces it with appropriate answer.

    Arguments:
    - `numbers`: List of integers

    Returns
    - `numbers`: List of strings
    """
    if type(numbers) != list:
        raise Exception("Numbers must be a list")
    

    size = len(numbers)
    j = 0

    while j < size:
        if type(numbers[j]) != int:
            raise Exception("Numbers must be a list of integers")

        if numbers[j] % 3 == 0 and numbers[j] % 5 == 0:
            numbers[j] = "FizzBuzz"
        elif numbers[j] % 3 == 0:
            numbers[j] = "Fizz"
        elif numbers[j] % 5 == 0:
            numbers[j] = "Buzz"
        else:
            numbers[j] = str(numbers[j])
        j += 1

    return numbers



