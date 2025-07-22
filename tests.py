# from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
# test_1_result = get_files_info("calculator",".")
# test_2_result = get_files_info("calculator","pkg")
# test_3_result = get_files_info("calculator","/bin")
# test_4_result = get_files_info("calculator","../")

# print(test_1_result)
# print(test_2_result)
# print(test_3_result)
# print(test_4_result)

test_1_result = get_file_content("calculator","main.py")
test_2_result = get_file_content("calculator","pkg/calculator.py")
test_3_result = get_file_content("calculator","/bin/cat")
test_4_result = get_file_content("calculator","pkg/does_not_exist.py")

print(test_1_result)
print(test_2_result)
print(test_3_result)
print(test_4_result)