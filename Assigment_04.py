# ---------- Task - 01 ---------- 

file_path = r'C:\Users\parth\Downloads\python learn\errors.txt'


def func(file_path):
    try:
        file = open(file_path)
        line_number = 1
        for line in file:
            print(f"Line {line_number}:",line.strip())
            line_number += 1
    except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")

func(file_path)



# ----------------------------------------------------------------------------------------

# ---------- Task - 02 ---------- 


file_path = r'C:\Users\parth\Downloads\python learn\errors.txt'

strings1 = input("Enter text to write it to the file: ")

with open(file_path, 'a') as file:
    file.write('\n' + strings1)
    print('Data succesfully appended')

strings2 = input("Enter additional text to append: ")

with open(file_path, 'a') as file:
    file.write('\n' + strings2)
    print('Data succesfully appended')

with open(file_path, 'r') as file:
    print(f'Final content of {file_path}')
    print(file.read())