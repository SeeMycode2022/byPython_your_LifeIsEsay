
def decimal_to_binary(decimal_num):
    binary_str = bin(decimal_num)[2:]  
    return binary_str

def decimal_to_octal(decimal_num):
    octal_str = oct(decimal_num)[2:]  
    return octal_str

def decimal_to_hexadecimal(decimal_num):
    hexadecimal_str = hex(decimal_num)[2:]  
    return hexadecimal_str.upper()  

def convert_to_decimal(number_str, base_str):
    decimal_num = int(number_str, base_str)
    return decimal_num
   