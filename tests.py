from functions.get_files_info import get_files_info

test_1_result = get_files_info("calculator",".")
test_2_result = get_files_info("calculator","pkg")
test_3_result = get_files_info("calculator","/bin")
test_4_result = get_files_info("calculator","../")

print(test_1_result)
print(test_2_result)
print(test_3_result)
print(test_4_result)