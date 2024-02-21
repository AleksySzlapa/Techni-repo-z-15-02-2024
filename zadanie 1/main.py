def file_sumer(file_path):
    with open(file_path) as my_file:
        data = my_file.read().split(';')
        if data[0] != '':
            temp = 0
            for element in data:
                if int(element) not in range (-10, 10):
                    return
                else:
                    temp += int(element)

            return temp
        else:
            return 0
print(file_sumer('test2.txt'))