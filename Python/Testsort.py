import re

def main():
    correct_file_location = input("Please input the location of the correct file to open: ")
    wrong_file_location = input("Please input the location of the wrong file to open: ")

    try:
        with open(correct_file_location, "r") as correct_fileOpen:
           print("1")

        with open(wrong_file_location, "r") as wrong_fileOpen:
            print("2")

    except FileNotFoundError:
        print("File not found. Please check the file location.")

if __name__ == "__main__":
    main()
