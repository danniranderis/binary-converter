# coding: utf-8
"""
Lib for various conversions på binary-numbers to and from decimal-numbers
"""
from __future__ import unicode_literals

import sys

__author__ = "Danni Randeris, danni@danniranderis.dk"

    
def binary_to_decimal(number):
    """ Converts a binary-number to decimal-number """
    return int(number, 2)


def decimal_to_binary(number):
    """ Converts a decimal-number to its binary representation """
    # FIXME: Not the best way to do it - it's dirty, but works for now
    return bin(int(number))[2:]


def ipv4_to_binary(number):
    """ Converts a dotted IPv4 to its binary representation """
    binary_num = []
    # Split the number into its 4 octet's and convert the numbers
    for octet in number.split('.'):
        binary_num.append(decimal_to_binary(octet))
    return '.'.join(binary_num)


def binary_ipv4_to_ipv4(number):
    """ Converts a dotted IPv4 in binary to its decimal representation """
    dec_num = []
    # Split the number into its 4 octet's and convert the numbers
    for octet in number.split('.'):
        dec_num.append(binary_to_decimal(octet))
    return '.'.join(str(x) for x in dec_num)


def convert_file(file_path=None, input_type=None):
    """
    Read a files lines and convert all decimal-numbers (one-per-line), then
    print the result.
    
    @param file_path: path to file for looping over
    @param input_type: define the input format [dec|bin|ip] and output
        vise-versa
    """
    with open(file_path) as f:
        for line in f:
            # Strip newline-chars
            line = line.strip('\n')
            
            # FIXME: rewrite to use python class-based and extends
            # Create output
            if input_type == 'dec':
                output_number = decimal_to_binary(line)
            elif input_type == 'bin':
                output_number = binary_to_decimal(line)
            elif input_type == 'ip':
                output_number = ipv4_to_binary(line)
            elif input_type == 'ip_bin':
                output_number = binary_ipv4_to_ipv4(line)
            
            print('{unconverted_number} = {output}'.format(
                unconverted_number=line,
                output=output_number))


if __name__ == '__main__':
    # Only if the file is called (not just imported), then do the conversion
    
    # Extract args given the script at run
    try:
        file_path_arg = sys.argv[1]
        input_type_arg = sys.argv[2]
    except IndexError:
        print('You have to provide a path to a txt-file af first args. The '
              'second args has to be a str: dec|bin|ip|ip_bin')

    # Define if we only need to convert a single number, or a whole file

    convert_file(file_path_arg, input_type_arg)
