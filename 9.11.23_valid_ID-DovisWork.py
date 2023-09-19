def is_valid_id(id_num):
    check_sum = 0
    for index, digit in enumerate(id_num):
        num_val = int(digit) * (index % 2 + 1)
        check_sum += num_val // 10 + num_val % 10
    return check_sum % 10 == 0
