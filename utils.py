import re

def count_alpha_numerics(inputstr:str):
    count = sum(char.isalnum() for char in inputstr)
    return count

def get_selection_column(position):
    is_on_right_half=False
    if position > 41:
        is_on_right_half=True
    position%=41
    column = position//5
    if is_on_right_half == True:
        column+=8
    return column

def string_to_hex(string):
    hex_values = string.strip()
    hex_values = hex_values.replace(' ','')
    hex_values = hex_values.replace('\n','')
    hex_values = bytearray.fromhex(hex_values)
    return hex_values

def is_end_of_byte(position):
    position%=81
    position%=41
    position-=1
    if position%5 == 2:
        return True
    return False


def is_end_of_line(position):
    position%=81
    if position>=79:
        return True
    return False

def get_byte_position(position):
    row = position//81
    column = position%81
    is_on_right_half = True if column > 41 else False
    column %= 41
    column //= 5
    return row*81 + is_on_right_half*41 + column*5 + 1

def get_hex_position(row,column):
    is_on_right_half = True if column>7 else False
    column%=8
    return row*81 + is_on_right_half*41 + column*5 + 1
