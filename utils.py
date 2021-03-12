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
