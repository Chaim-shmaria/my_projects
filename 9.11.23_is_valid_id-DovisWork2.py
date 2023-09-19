def is_valid_id(id_num):
    return sum([(int(digit) * (index % 2 + 1) // 10 + int(digit) * (index % 2 + 1) % 10) for index, digit in
                enumerate(id_num)]) % 10 == 0
