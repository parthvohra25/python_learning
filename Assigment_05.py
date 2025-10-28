# ---------- Task - 01 ---------- 

# class_students = {
#     "Alice": 25,
#     "Bob": 57,
#     "Candice": 98
# }
# # print(class_students)

# name = input("Enter the student's name: ")

# if name in class_students:
#     print (f"{name}'s marks: {class_students[name]}")
# else:
#     print("Student not found.")

# ----------------------------------------------------------------------------------------

# ---------- Task - 02 ---------- 

original_list = [i+1 for i in range(10)]

print("Original List: ",original_list)
print("Extracted first five elements: ",original_list[:5])
print("Reverse extracted elements: ",original_list[4::-1])