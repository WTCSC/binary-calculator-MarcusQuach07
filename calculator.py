# Creates a variable called binary_to_decimal that takes in a binary number and converts it to decimal
def binary_to_decimal(binary):

    # Checks if length is valid for a 8 bit binary number and if all bits are either 0 or 1
    if len(binary) != 8 or not all(bit in ['0', '1'] for bit in binary):
        # Returns error message if binary number is not valid
        return "Error"
    # Argument to store decimal number, set as 0
    decimal = 0
        
    # For loop for i in a range of 0-7
    for i in range(8):
         # Equation for binary to decimal conversion
        decimal += int(binary[i]) * (2 ** (7 - i))
    # Returns decimal number
    return decimal

# Creates a variable called decimal_to_binary that takes in a decimal number and converts it to binary
def decimal_to_binary(decimal):

    # Checks if decimal is smaller than 0 or greater than 255
    if decimal < 0 or decimal > 255:
        # Returns error message if decimal is not within the valid range for 8-bit binary
        return "Overflow"
        
    # Empty argument to store binary number
    binary = ""
        
    # For loop for i in a range of 0-7 and goes in reverse order
    for i in range(7, -1, -1):
            
        # if decimal is greater than or equal to 2 to the power of i
        if decimal >= 2 ** i:
            # Adds 1 to the binary number
            binary += "1"
            # Subtracts 2 to the power of i from the decimal
            decimal -= 2 ** i
                # else adds 0 to the binary number
        else:
            binary += "0"
            # Fill the binary number with 0s to make it 8 bits
            return binary.zfill(8)



# Creates variable called binary_calculator that takes in 3 arguments: bin1, bin2, and operator
def binary_calculator(bin1, bin2, operator):

    # Checks if length is valid for a 8 bit binary number and if all bits are either 0 or 1
    if len(bin1) != 8 or len(bin2) != 8 or not all(bit in ['0', '1'] for bit in bin1 + bin2):
        # Returns error message if binary number is not valid
        return "Error" 

    # Takes bin1 and bin2 and converts them to integers using the binary_to_decimal function
    num1 = binary_to_decimal(bin1)
    num2 = binary_to_decimal(bin2)

    # Checks if conversion is possible
    if isinstance(num1, str) or isinstance(num2, str):
        #returns error if conversion is not possible
        return "Error"
    
    # Takes operator and checks if it is a valid operator
    # Then takes num1 and num2 and performs the operation
    if operator == '+':
        result = num1 + num2
        
    elif operator == '-':
        result = num1 - num2

    elif operator == '*':
        result = num1 * num2

    elif operator == '/':
        if num2 == 0:
            # Returns error message if division by 0 is attempted
            return "NaN"
        # Floors the numbers to get the whole number so it can be turned into binary
        result = num1 // num2
    else:
        # Wont take any other operators
        return "Error"

# Overflow Check
# Checks if result is less than 0 or greater than 255
    if result < 0 or result > 255:
    # Returns error message if result is not within the valid range for 8-bit binary
        return "Overflow"
    # Returns the result in binary
    return decimal_to_binary(result)
