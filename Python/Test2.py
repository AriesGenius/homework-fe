import re

def process_data(correct_filelocation,wrong_filelocation):
    answer_array = []
    user_answer_array = []

    # Your data processing logic here...

    with open(correct_filelocation, "r") as correct_fileOpen:
        
                

        return answer_array
    with open(wrong_filelocation, "r") as wrong_fileOpen:
        return user_answer_array
    

def main():
    correct_filelocation = input("Please input the location of the correct file to open: ")
    answer_array = process_data(correct_filelocation)

    for item in answer_array:
        print(item)

if __name__ == "__main__":
    main()
