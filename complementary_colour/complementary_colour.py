# Find RGB complementary colour

def check_values(value):
    """
    check_values(value, colour)

    Checks whether given value is not below 0 and not greater than 255.

    Arguments:
    - `value`: Single value (red/green/blue) 0-255
    """
    if value < 0 or value > 255:
        raise Exception("Value must be an integer between 0 and 255.")

def get_complementary_colour(red, green, blue):
    """
    get_complementary_colour(red, green, blue)

    Calculates the complementary RGB value of given RGB values.

    Arguments:
    - `red`: (Int) red value 0-255
    - `green`: (Int) green value 0-255
    - `blue`: (Int) blue value 0-255

    Returns:
    List
        - `complementary_red`: red value of complementary colour 0-255
        - `complementary_green`: green value of complementary colour 0-255
        - `complementary_blue`: blue value of complementary colour 0-255
    """

    check_values(red)
    check_values(green)
    check_values(blue)

    complementary_red = 255 - red
    complementary_green = 255 - green
    complementary_blue = 255 - blue

    return complementary_red, complementary_green, complementary_blue



if __name__ == "__main__":
    red = int(input("Enter red: "))

    green = int(input("Enter green: "))

    blue = int(input("Enter blue: "))

    complementary_colour = get_complementary_colour(red, green, blue)

    print("Your complementary colour is:")
    print("R:", complementary_colour[0])
    print("G:", complementary_colour[1])
    print("B:", complementary_colour[2])
