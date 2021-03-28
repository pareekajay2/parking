from transport import process_command
from utilities.InputFileValidator import FileValidator


def read_input():
    while True:
        filename = "file_utilities/" + input("Enter your file name: ", )
        with open(filename, 'r') as file:
            content = file.read()
            file_validator = FileValidator(content=content)
            file_validator.is_valid()
            process_command(content.split("\n"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_input()

