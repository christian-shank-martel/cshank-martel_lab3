#!/usr/bin/env python3
#Author: christian shank-martel
#Date:feb 15th 2023
#Program: Lab3.py


def write_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f=open(file_name, 'w')
    f.write(string_of_lines)
    f.close


if __name__ == '__main__':
    file1 = 'Lab5_part2_III'
    string1 = 'christian shank-martel'
    write_file_string(file1, string1)
