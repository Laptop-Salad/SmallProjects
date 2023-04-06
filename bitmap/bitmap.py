"""
Create a customized bitmap of the world.
"""

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""
print("Bitmap Message")
print("Enter the message to display with the bitmap.")

message = input(">")
message = list(message)
current_char = 0

split = bitmap.splitlines(True)

# Iterate through lines
for line in range(0, len(split)):
    # Iterate through characters
    for char in range(0, len(split[line])):
        # If character isnt a whitespace
        if split[line][char] == "*" or split[line][char] == ".":
            print(message[current_char], end="")
            
            # Move character in message up by 1
            current_char += 1
            
            # If the current character in message is the last, reset to 0
            if current_char == len(message):
                current_char = 0
        else:
            # Otherwise print a whitespace
            print(" ", end="")
    print()
    
print("Made out of pure 100 {} organic {}".format("%", ''.join(message)))
