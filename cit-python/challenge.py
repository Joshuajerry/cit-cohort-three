# function that finds the maximum number in a ist

def find_max(sample_list: list) -> int:
    max_num = 0
    for num in sample_list:
        if num > max_num:
            max_num = num
            
    return max_num

sample = [4, 987, 2, 3, 8, 98, 567]
print(find_max(sample))
    
    