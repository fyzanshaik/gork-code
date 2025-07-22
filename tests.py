# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python import run_python_file



# test_1_result = get_files_info("calculator",".")
# test_2_result = get_files_info("calculator","pkg")
# test_3_result = get_files_info("calculator","/bin")
# test_4_result = get_files_info("calculator","../")

# print(test_1_result)
# print(test_2_result)
# print(test_3_result)
# print(test_4_result)

# test_1_result = get_file_content("calculator","main.py")
# test_2_result = get_file_content("calculator","pkg/calculator.py")
# test_3_result = get_file_content("calculator","/bin/cat")
# test_4_result = get_file_content("calculator","pkg/does_not_exist.py")

# print(test_1_result)
# print(test_2_result)
# print(test_3_result)
# print(test_4_result)

# test_1_result = write_file("calculator","lorem.txt", "wait, this isn't lorem ipsum")
# test_2_result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# test_3_result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# # test_4_result = write_file("calculator","pkg/does_not_exist.py")

# print(test_1_result)
# print(test_2_result)
# print(test_3_result)
# # print(test_4_result)


test_1_result = run_python_file("calculator","main.py")
test_2_result = run_python_file("calculator", "main.py", ["3 + 5"])
test_3_result = run_python_file("calculator", "tests.py")
test_4_result = run_python_file("calculator", "../main.py")
test_5_result = run_python_file("calculator", "nonexistent.py")

print(test_1_result)
print(test_2_result)
print(test_3_result)
print(test_4_result)
print(test_5_result)