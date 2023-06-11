import argparse
import re

parser = argparse.ArgumentParser(description = "Hola")
parser.add_argument("-i", "--input_file", default = None, help = ("Input file to read"))
parser.add_argument("-o", "--output_file", default = None, help = ("Output file"))
parser.add_argument("-l", "--length", action="store_true", default = None, help = ("Length of of file"))
parser.add_argument("-n", "--number_true", action="store_true", default = None, help = ("Are there numbers in the file"))

args = parser.parse_args()

def open_file(input_file):
    file = open(input_file, encoding='utf-8')
    content = file.read()
    file.close()
    return content

def capitals(input_file):
    """Switch text into capital letters"""
    output_file = input_file.upper()
    return output_file

def write_output(output_file, new_content):
    with open(output_file, mode = 'w', encoding = 'utf-8') as output:
        output.write(new_content)

def length_file(file):
    file_length = len(file)
    return file_length

def number_in_file(text):
    return re.search(r'\d', text)


def main(input, output, length = False, contains_num = False):
    file_value = open_file(input)
    new_file_content = capitals(file_value)
    if contains_num:
        if number_in_file(file_value):
            new_file_content += "\nThe file contains numbers."
        else:
            new_file_content += "\nThe file does not contain numbers."
    if length:
        file_length = length_file(file_value)
        new_file_content += f"\nLength of the file: {file_length}"
    write_output(output, new_file_content)

main(args.input_file,args.output_file, args.length,args.number_true)